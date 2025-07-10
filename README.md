A real-time AI-powered system for face detection, recognition, tracking, logging, and unique visitor counting using YOLOv8, InsightFace, and Python.

💡 Features : 
✅ Real-time face detection using YOLOv8
✅ Face recognition with InsightFace / ArcFace
✅ Auto-registration of new visitors with unique ID
✅ Accurate entry/exit logging with timestamps
✅ Saves cropped face images locally by date
✅ Stores logs in CSV and SQLite database
✅ Unique visitor counter to avoid duplicate counts

🛠️ Technologies Used
-> Python 3.10
-> OpenCV
-> YOLOv8 (Ultralytics)
-> InsightFace
-> SQLite (via sqlite3)
-> Pandas
-> NumPy
-> Tkinter (optional for viewing logs)


📦 Setup Instructions
1. Clone the Repository
    ```bash
     git clone https://github.com/Abhinayapriya/Intelligent-Face-Tracker-.git
     cd Intelligent-Face-Tracker-
    ```
   
2. Create Virtual Environment
   ```bash
     python -m venv venv
   ```
   
4. Activate Virtual Environment
   -> Windows:
   ```bash
    venv\Scripts\activate
   ```
   -> Linux / macOS:
   ```bash
   source venv/bin/activate
   ```
   
6. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
   
8. Run the Application
    ```bash
   python main.py
   ```
    
10. View Visitor Logs
    ```bash
    python view_log.py
    ```

⚙️ Sample config.json 
  -> json
  ```bash
{
  "video_source": "myvideos.mp4",
  "frame_skip": 5,
  "detection_confidence": 0.6
}
```

🗂️ Project Folder Structure
📁 Intelligent-Face-Tracker-/
├── config.json
├── database.py
├── detector.py
├── logger.py
├── main.py
├── recognizer.py
├── view_log.py
├── yolov8n-face.pt
├── visitor_logs.db
├── faces/
│   └── entry/YYYY-MM-DD/*.jpg
├── logs/
│   └── log.csv
└── README.md

🧪 Assumptions Made
-> Faces present for only a few frames are not registered.
-> Cropped face images are saved only for entries, not exits.
-> If the same face disappears and reappears after a long gap, it might be treated as a new person.
-> Unique ID is assigned as person_<frame_number>_<face_number> for simplicity.

📈 Sample Output
✅ Log file example:
```bash 
    -> person_1_0, entry, 2025-07-09 19:20:22  
    -> person_1_0, exit, 2025-07-09 19:20:45
```
✅ Cropped face saved:
```bash
   -> faces/entry/2025-07-09/person_1_0_20250709_192022.jpg
```
✅ Total unique visitors:
```bash
   -> Total unique visitors: 24
```
“This project is a part of a hackathon run by https://katomaran.com
