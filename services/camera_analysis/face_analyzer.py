import cv2
import mediapipe as mp
import numpy as np


class FaceAnalyzer:

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process_frame(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_mesh.process(rgb_frame)

        return results

    def analyze_frame(self, frame):

        results = self.process_frame(frame)

        # No face detected
        if not results.multi_face_landmarks:
            return {
                "face_detected": False,
                "centered": False,
                "face_size": 0,
                "yaw": 0,
                "pitch": 0,
                "roll": 0,
                "camera_facing": False
            }

        landmarks = results.multi_face_landmarks[0].landmark

        h, w, _ = frame.shape

        # ------------------------------------------------
        # 1. Find face bounding box
        # ------------------------------------------------

        x_coordinates = [
            landmark.x for landmark in landmarks
        ]

        y_coordinates = [
            landmark.y for landmark in landmarks
        ]

        min_x = max(0, min(x_coordinates))
        max_x = min(1, max(x_coordinates))

        min_y = max(0, min(y_coordinates))
        max_y = min(1, max(y_coordinates))

        face_width = max_x - min_x
        face_height = max_y - min_y

        face_size = face_width * face_height

        # ------------------------------------------------
        # 2. Face center
        # ------------------------------------------------

        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        centered = (
            0.30 <= center_x <= 0.70 and
            0.25 <= center_y <= 0.75
        )

        # ------------------------------------------------
        # 3. Head pose estimation
        # ------------------------------------------------

        yaw, pitch, roll = self.calculate_head_pose(
            landmarks,
            w,
            h
        )

        # ------------------------------------------------
        # 4. Camera-facing estimation
        # ------------------------------------------------

        camera_facing = (
            abs(yaw) < 20 and
            abs(pitch) < 20
        )

        return {
            "face_detected": True,
            "centered": centered,
            "face_size": round(face_size, 4),
            "center_x": round(center_x, 3),
            "center_y": round(center_y, 3),
            "yaw": round(yaw, 2),
            "pitch": round(pitch, 2),
            "roll": round(roll, 2),
            "camera_facing": camera_facing
        }

    def calculate_head_pose(self, landmarks, width, height):

        # Important MediaPipe landmarks
        #
        # 1   = nose
        # 33  = left eye region
        # 263 = right eye region
        # 61  = left mouth
        # 291 = right mouth
        # 152 = chin

        image_points = np.array([
            self.get_point(landmarks[1], width, height),     # Nose
            self.get_point(landmarks[152], width, height),   # Chin
            self.get_point(landmarks[33], width, height),    # Left eye
            self.get_point(landmarks[263], width, height),   # Right eye
            self.get_point(landmarks[61], width, height),    # Left mouth
            self.get_point(landmarks[291], width, height)    # Right mouth
        ], dtype=np.float64)

        # Approximate 3D face model
        model_points = np.array([
            (0.0, 0.0, 0.0),           # Nose
            (0.0, -63.6, -12.5),       # Chin
            (-43.3, 32.7, -26.0),      # Left eye
            (43.3, 32.7, -26.0),       # Right eye
            (-28.9, -28.9, -24.1),     # Left mouth
            (28.9, -28.9, -24.1)       # Right mouth
        ])

        focal_length = width

        center = (
            width / 2,
            height / 2
        )

        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype=np.float64)

        dist_coeffs = np.zeros(
            (4, 1),
            dtype=np.float64
        )

        success, rotation_vector, translation_vector = cv2.solvePnP(
            model_points,
            image_points,
            camera_matrix,
            dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:
            return 0.0, 0.0, 0.0

        rotation_matrix, _ = cv2.Rodrigues(
            rotation_vector
        )

        pose_matrix = np.hstack(
            (rotation_matrix, translation_vector)
        )

        _, _, _, _, _, _, euler_angles = cv2.decomposeProjectionMatrix(
            pose_matrix
        )

        pitch = float(euler_angles[0])
        yaw = float(euler_angles[1])
        roll = float(euler_angles[2])

        return yaw, pitch, roll

    @staticmethod
    def get_point(landmark, width, height):

        return (
            landmark.x * width,
            landmark.y * height
        )

    def close(self):

        self.face_mesh.close()