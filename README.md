# **SkyGuard – AI-Enabled Swarm Defense Drone System**

### *Autonomous Multi-Drone Swarm for Intruder Detection, Tracking & Interception*

---

##  **Overview**

**SkyGuard** is an AI-powered autonomous drone defense system designed to detect, track, and intercept unauthorized UAVs entering restricted airspace.  
Using **YOLOv8 computer vision**, **multi-agent swarm coordination**, and **Microsoft AirSim**, SkyGuard simulates how defender drones collaborate to neutralize intruder drones **without GPS or internet**.

SkyGuard demonstrates how **edge AI + swarm robotics** can provide scalable, low-cost counter-drone security for:

- Border surveillance  
- Airport protection  
- Military bases  
- Critical infrastructure  
- Autonomous monitoring zones  

---

##  **Core Features**

| Module                           | Description                                                       |
| -------------------------------- | ----------------------------------------------------------------- |
| **Real-time Intruder Detection** | YOLOv8-based object detection from drone cameras                  |
| **Swarm Coordination**           | Multi-agent communication + Randomized Intercept Algorithm (RIA)  |
| **Autonomous Navigation**        | AirSim flight physics, dynamic path planning & safety controls    |
| **Simulation Environment**       | Photorealistic Unreal Engine Blocks world                         |
| **Data Logging & Visualization** | CSV flight logs + Matplotlib trajectory plotting                  |
| **Hardware Friendly**            | Supports Jetson Nano, Raspberry Pi 5, Intel Movidius              |

---

##  **System Architecture**
                 ┌────────────────────────────┐
                 │      Perception Layer       │
                 │   (YOLOv8 Drone Detection)  │
                 └──────────────┬─────────────┘
                                │
          ┌─────────────────────┼──────────────────────┐
          │                     │                      │
┌─────────▼────────┐   ┌────────▼────────┐   ┌─────────▼────────┐
│  Communication    │   │   Control &     │   │ Randomized        │
│  (Broadcast Msg)  │   │ Navigation       │   │ Intercept Alg.    │
└─────────┬────────┘   └────────┬────────┘   └─────────┬────────┘
          │                     │                        │
          └───────────────┬────┴──────┬─────────────────┘
                          │           │
                ┌─────────▼──┐   ┌────▼────────┐
                │ Defender 0 │   │ Defender 1   │
                └────────────┘   └──────────────┘

                ┌────────────────────────────┐
                │     AirSim Environment     │
                │  (Simulation + Physics)    │
                └────────────────────────────┘

---

##  **Tech Stack**

### **Software**
- YOLOv8 (Ultralytics)
- Microsoft AirSim (Unreal Engine)
- Python 3.10
- OpenCV, NumPy, Matplotlib
- ZeroMQ (custom broadcast communication)
- Windows & Linux Support

### **Hardware Compatibility**
- NVIDIA Jetson Nano  
- Raspberry Pi 4 / 5  
- Intel Movidius NCS2  
- Lightweight quadcopter frames  

---

##  **Project Structure**
SkyGuard/
│
├── sim_runner.py # Main simulation controller
├── airsim_env.py # Drone movement, control & sensor wrapper
├── perception.py # YOLOv8 detection module
├── comms.py # Drone-to-drone communication system
├── qmix_trainer.py # Optional RL training module
├── trainer.py # Training utilities
├── visualize.py # Path & trajectory visualization tool
│
├── logs/ # CSV trajectory logs
├── results/ # Plots & detection images
├── models/ # YOLOv8 weights (e.g., yolov8n.pt)
├── settings.json # AirSim multi-drone configuration
└── README.md # Documentation

---

##  **How SkyGuard Works**

Step 1 — Launch AirSim
```powershell
cd "C:\Users\YourName\Documents\AirSim\Blocks\WindowsNoEditor"
.\Blocks.exe
Step 2 — Run Simulation
python sim_runner.py
Step 3 — Live Behavior
-->Defender drones take off
-->YOLOv8 begins scanning for intruders
-->Once detected → drones switch to intercept mode
-->Flight paths logged & plotted

## **Defender Swarm Interception Logic (RIA)**

SkyGuard uses a decentralized Randomized Intercept Algorithm (RIA) for smart multi-drone interception:

Nearest drone becomes the Leader

Leader moves directly toward the intruder

Support drones take random offset positions

Swarm forms a 360° containment ring

Interception occurs when distance < threshold

Produces non-linear, unpredictable pursuit paths—very effective in stopping hostile drones.

---

## 🌍 **Real-World Scalability**

SkyGuard is designed for future real-world deployment with:

✔ **Edge AI inference** (Jetson Nano, Raspberry Pi 5, Movidius)  
✔ **Thermal + LiDAR + Radar fusion** for all-weather detection  
✔ **Encrypted mesh networking** resistant to jamming  
✔ **GPS-denied navigation** using Visual SLAM / VIO  
✔ Swarm expansion up to **5–10 autonomous defender drones**

---

## 🔥 **Future Enhancements**

- Reinforcement Learning (RL)–based intelligent interception  
- Multi-sensor fusion (RGB + IR + LiDAR + Radar)  
- Long-range secure swarm-to-swarm communication  
- Outdoor-tested rugged hardware prototypes  
- Integration with border surveillance & defense systems  



