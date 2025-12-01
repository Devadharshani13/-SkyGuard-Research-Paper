# Aegis-Swarm — Hackathon Demo (Ready-to-run)

## Folder structure
Aegis-Swarm/
├─ airsim_env.py
├─ perception.py
├─ comms.py
├─ sim_runner.py
├─ trainer.py
├─ qmix_trainer.py
├─ visualize.py
├─ requirements_win.txt
├─ run_demo.bat
├─ logs/
├─ plots/
├─ models/
└─ README.md

## Quick start (Windows)
1. Ensure AirSim Blocks is downloaded & extracted. Blocks.exe should be at:
   `C:\Users\sriram\Documents\AirSim\Blocks\WindowsNoEditor\Blocks.exe`

2. Create Python venv in project folder:
   ```powershell
   cd C:\Users\sriram\Documents\Desktop\skygaurd
   python -m venv venv
   .\venv\Scripts\activate
