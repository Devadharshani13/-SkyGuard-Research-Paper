"""
sim_runner.py — Main SkyGuard Simulation Runner
Now includes live YOLO detection and OpenCV visualization.
"""

import time
import random
from airsim_env import AirSimEnv

def main():
    print("\n🚀 Launching SkyGuard Simulation Demo with Live View...\n")

    # Initialize environment
    env = AirSimEnv(['defender0', 'defender1', 'intruder'])

    drone_ids = ["defender0", "defender1"]
    intruder_id = "intruder"
    print(f"[INFO] Defender drones ready: {drone_ids}")
    print(f"[INFO] Intruder initialized for movement.\n")

    # Main simulation loop
    for step in range(1, 16):
        print(f"\n[STEP {step}] =============================")

        # Move intruder randomly
        move_x = random.uniform(1, 3)
        move_y = random.uniform(-1, 1)
        env.move_drone(intruder_id, move_x, move_y, 0, duration=1)

        # Capture and detect from defender0
        result = env.capture_frame(drone_ids[0], detect=True, show=True)
        if result is None:
            print("[INFO] No frame received, skipping detection.")
            continue

        frame, detections = result
        boxes = detections[0].boxes if hasattr(detections[0], 'boxes') else []

        if len(boxes) > 0:
            print(f"[ALERT] Intruder detected ({len(boxes)} objects)!")
            # Move drones to intercept (simple reaction)
            env.move_to(drone_ids[0], (20, 0, -10))
            env.move_to(drone_ids[1], (15, 5, -10))
        else:
            print("[INFO] No intruder detected, patrolling...")

        time.sleep(1)

    # Wrap up simulation
    env.land_all()
    print("\n✅ Simulation complete! Live view closed.\n")


if __name__ == "__main__":
    main()
