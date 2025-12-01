"""
perception.py
YOLOv8-based target detection for Aegis-Swarm demo.
Detects intruder drones using Ultralytics YOLOv8 model.
"""

from ultralytics import YOLO
import cv2
import numpy as np
import torch

class YOLOv8Perception:
    def __init__(self, model_path="yolov8n.pt", conf=0.5):
        self.model = YOLO(model_path)
        self.conf = conf
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[INFO] YOLOv8 initialized on {self.device}")

    def detect_intruder(self, frame):
        """
        Run YOLOv8 detection on the given image frame.
        Returns bounding boxes and confidence scores for detected intruders.
        """
        results = self.model.predict(frame, conf=self.conf, device=self.device, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls)
                label = self.model.names[cls_id]
                conf = float(box.conf)
                if "drone" in label.lower() or "quad" in label.lower():
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append({"label": label, "conf": conf, "bbox": (x1, y1, x2, y2)})

        return detections

    def visualize(self, frame, detections):
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{det['label']} {det['conf']:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        return frame


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # webcam test
    detector = YOLOv8Perception()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detections = detector.detect_intruder(frame)
        vis = detector.visualize(frame, detections)
        cv2.imshow("YOLOv8 Detection", vis)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
