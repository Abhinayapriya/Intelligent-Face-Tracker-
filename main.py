import os
import cv2
import csv
from datetime import datetime
from detector import FaceDetector
from database import init_db, log_to_db  # ✅ Import DB function

# --- INIT DB ---
init_db()

# --- SETTINGS ---
VIDEO_DIR = "myvideos.mp4"
OUTPUT_DIR = "faces/entry"
LOG_FILE = "log.csv"

# --- Ensure folders exist ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Logging function ---
def log_event(visitor_id, event_type, image_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([visitor_id, event_type, timestamp])

    # ✅ Log to SQLite database
    log_to_db(visitor_id, event_type, timestamp, image_path)

# --- Check for videos ---
if not os.path.exists(VIDEO_DIR):
    print("❌ No video file or folder found.")
    exit()

video_files = []
if os.path.isdir(VIDEO_DIR):
    video_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith((".mp4", ".avi", ".mov"))]
elif os.path.isfile(VIDEO_DIR):
    video_files = [VIDEO_DIR]

if not video_files:
    print("❌ No video files found.")
    exit()

# --- Load detector ---
detector = FaceDetector()

# --- Process videos ---
for video_file in video_files:
    video_path = os.path.join(VIDEO_DIR, video_file) if os.path.isdir(VIDEO_DIR) else video_file
    print(f"\n▶ Processing: {video_path}")
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

        detections = detector.detect_faces(frame)
        if detections is None:
            continue

        for i, (x1, y1, x2, y2, conf) in enumerate(detections):
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Crop and save face
            face_crop = frame[y1:y2, x1:x2]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            visitor_id = f"person_{frame_count}_{i}"
            save_path = os.path.join(OUTPUT_DIR, f"{visitor_id}_{timestamp}.jpg")
            cv2.imwrite(save_path, face_crop)

            # ✅ Log entry to both CSV and DB
            log_event(visitor_id, "entry", save_path)

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
