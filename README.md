
# **SkyGuard – AI-Enabled Swarm Defense Drone System**
### *Autonomous Multi-Drone Swarm for Intruder Detection, Tracking & Interception*

---

## 🚀 **Overview**

**SkyGuard** is an AI-powered autonomous drone defense system designed to detect, track, and intercept unauthorized UAVs entering restricted airspace.  
Using **YOLOv8 computer vision**, **multi-agent swarm coordination**, and **Microsoft AirSim**, SkyGuard demonstrates how defender drones collaborate to neutralize intruders **without GPS or internet**.

Built as a scalable, low-cost edge-AI defense solution for:

- Border surveillance  
- Airport protection  
- Military bases  
- Critical infrastructure  
- Autonomous monitoring zones  

---

## 🎯 **Core Features**

| Module                           | Description                                                       |
| -------------------------------- | ----------------------------------------------------------------- |
| **Intruder Detection**           | YOLOv8-based drone detection                                      |
| **Swarm Coordination**           | Broadcast communication + Randomized Intercept Algorithm (RIA)    |
| **Autonomous Navigation**        | AirSim movement, physics & path control                           |
| **Simulation Environment**       | Unreal Engine Blocks aerial world                                 |
| **Data Logging & Visualization** | CSV logs + trajectory plotting                                    |
| **Edge Hardware Ready**          | Jetson Nano, Raspberry Pi 5, Movidius support                     |

---

## 🧠 **System Architecture**

```

```
             ┌────────────────────────────┐
             │      Perception Layer       │
             │   (YOLOv8 Drone Detection)  │
             └──────────────┬─────────────┘
                            │
      ┌─────────────────────┼──────────────────────┐
      │                     │                      │
```

┌─────────▼────────┐   ┌────────▼────────┐   ┌─────────▼────────┐
│  Communication    │   │   Control &     │   │ Randomized        │
│  (Broadcast Msg)  │   │   Navigation     │   │ Intercept Alg.    │
└─────────┬────────┘   └────────┬────────┘   └─────────┬────────┘
│                     │                        │
└───────────────┬────┴──────┬─────────────────┘
│           │
┌─────────▼──┐   ┌────▼────────┐
│ Defender 0 │   │ Defender 1   │
└────────────┘   └──────────────┘

```
            ┌────────────────────────────┐
            │     AirSim Environment     │
            │  (Simulation + Physics)    │
            └────────────────────────────┘
```

```

---

##  **Tech Stack**

### **Software**
- YOLOv8 (Ultralytics)
- Microsoft AirSim (Unreal Engine)
- Python 3.10
- OpenCV, NumPy, Matplotlib
- ZeroMQ / Custom Broadcast Messaging

### **Hardware**
- NVIDIA Jetson Nano  
- Raspberry Pi 4 / 5  
- Intel Movidius NCS2  
- Lightweight quadcopter frames  

---

##  **Project Structure**

```

SkyGuard/
│
├── sim_runner.py          # Main simulation controller
├── airsim_env.py          # Drone movement, sensors & control
├── perception.py          # YOLOv8 detection pipeline
├── comms.py               # Swarm communication system
├── qmix_trainer.py        # (Optional) RL training
├── trainer.py             # Training utilities
├── visualize.py           # Trajectory plotting
│
├── logs/                  # CSV flight logs
├── results/               # Detection images & plots
├── models/                # YOLOv8 weights (e.g., yolov8n.pt)
├── settings.json          # AirSim multi-drone configuration
└── README.md              # Documentation

````

---

##  **How SkyGuard Works**

### **Step 1 — Launch AirSim**
```powershell
cd "C:\Users\YourName\Documents\AirSim\Blocks\WindowsNoEditor"
.\Blocks.exe
````

### **Step 2 — Run Simulation**

```bash
python sim_runner.py
```

### **Step 3 — Autonomous Behavior**

* Defender drones take off
* YOLOv8 begins scanning
* Once intruder detected → drones switch to intercept mode
* Paths logged & plotted

---

##  **Defender Swarm Interception Logic (RIA)**

SkyGuard uses a decentralized algorithm for multi-drone interception:

* Nearest drone becomes **Leader**
* Leader approaches intruder directly
* Other drones take **random offset positions**
* Swarm forms a **360° containment ring**
* Interception occurs when distance < threshold

Produces **non-linear, unpredictable pursuit**—effective for anti-drone missions.

---

## 🌍 **Real-World Scalability**

SkyGuard supports future deployment through:

✔ Edge AI inference (Jetson / Pi)
✔ Thermal + LiDAR + Radar fusion
✔ Encrypted mesh networking
✔ GPS-denied SLAM navigation
✔ Expansion up to 5–10 defender drones

---

## 🔥 **Future Enhancements**

* Reinforcement learning–based interception
* Multi-sensor fusion (RGB + IR + LiDAR + Radar)
* Long-range secure communication
* Rugged outdoor-ready prototype
* Integration with border security systems




```
