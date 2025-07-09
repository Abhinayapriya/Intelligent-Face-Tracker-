from ultralytics import YOLO

class FaceDetector:
    def __init__(self):
        model_path = "yolov8n.pt"  # using general-purpose YOLOv8 model
        self.model = YOLO("yolov8n.pt")

    def detect_faces(self, frame):
        results = self.model(frame, verbose=False)[0]
        if results is None or results.boxes is None:
            return []
        
        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            detections.append((int(x1), int(y1), int(x2), int(y2), conf))
        return detections
