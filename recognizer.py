import insightface
import numpy as np

class FaceRecognizer:
    def __init__(self):
        self.model = insightface.app.FaceAnalysis(name='buffalo_l')
        self.model.prepare(ctx_id=0)
        self.known_faces = {}  # {person_id: embedding}

    def get_embedding(self, face_img):
        faces = self.model.get(face_img)
        if faces:
            return faces[0].embedding
        return None

    def register_or_recognize(self, embedding, threshold=0.6):
        for person_id, known_emb in self.known_faces.items():
            dist = np.linalg.norm(embedding - known_emb)
            if dist < threshold:
                return person_id  # Recognized
        # Not recognized → register new
        new_id = f"visitor_{len(self.known_faces)+1}"
        self.known_faces[new_id] = embedding
        return new_id
