import airsim
import time
import numpy as np
import cv2
from ultralytics import YOLO

class AirSimEnv:
    def __init__(self, drone_names, yolo_model="yolov8n.pt"):
        print("[INFO] Connecting to AirSim...")
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        print("Connected!")
        self.drone_names = drone_names

        # Load YOLOv8 model
        self.yolo = YOLO(yolo_model)
        print(f"[INFO] YOLOv8 initialized on {'cuda' if self.yolo.device != 'cpu' else 'cpu'}")

        # Arm and takeoff all drones
        for name in self.drone_names:
            self.client.enableApiControl(True, name)
            self.client.armDisarm(True, name)
            print(f"[INFO] Taking off {name}...")
            self.client.takeoffAsync(vehicle_name=name).join()
        print("[INFO] All drones are airborne and ready!")

    def capture_frame(self, drone_name, detect=False, show=False):
        """Capture a front-facing RGB image from a drone camera. Optionally detect and show."""
        try:
            responses = self.client.simGetImages([
                airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)
            ], vehicle_name=drone_name)

            if not responses or len(responses) == 0:
                return None

            img1d = np.frombuffer(responses[0].image_data_uint8, dtype=np.uint8)
            if img1d.size == 0:
                return None

            frame = img1d.reshape(responses[0].height, responses[0].width, 3)

            if detect:
                results = self.yolo(frame[..., ::-1])  # Convert RGB → BGR
                annotated = results[0].plot()
                if show:
                    cv2.imshow(f"{drone_name} - YOLO View", annotated)
                    cv2.waitKey(1)
                return annotated, results
            else:
                if show:
                    cv2.imshow(f"{drone_name} - Camera", frame)
                    cv2.waitKey(1)
                return frame
        except Exception as e:
            print(f"[ERROR] capture_frame() failed for {drone_name}: {e}")
            return None

    def move_drone(self, drone_name, x, y, z, duration=1):
        """Move drone by relative offset."""
        try:
            position = self.client.getMultirotorState(vehicle_name=drone_name).kinematics_estimated.position
            target = airsim.Vector3r(position.x_val + x, position.y_val + y, position.z_val + z)
            self.client.moveToPositionAsync(target.x_val, target.y_val, target.z_val, velocity=3, vehicle_name=drone_name).join()
            time.sleep(duration)
        except Exception as e:
            print(f"[ERROR] move_drone() failed for {drone_name}: {e}")

    def move_to(self, drone_name, target):
        """Move drone to an absolute position."""
        try:
            x, y, z = target
            self.client.moveToPositionAsync(x, y, z, velocity=3, vehicle_name=drone_name).join()
        except Exception as e:
            print(f"[ERROR] move_to() failed for {drone_name}: {e}")

    def land_all(self):
        """Safely land all drones."""
        for name in self.drone_names:
            print(f"[INFO] Landing {name}...")
            self.client.landAsync(vehicle_name=name).join()
            self.client.armDisarm(False, name)
            self.client.enableApiControl(False, name)
        print("[INFO] All drones landed and disarmed.")
        cv2.destroyAllWindows()
