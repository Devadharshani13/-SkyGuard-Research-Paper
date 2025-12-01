"""
Plot XY trajectories from logs/episode_demo.csv and save to plots/.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('plots', exist_ok=True)
csv_path = 'logs/episode_demo.csv'
if not os.path.exists(csv_path):
    print("[WARN] Log file not found:", csv_path)
else:
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(6,6))
    plt.plot(df['def0_x'], df['def0_y'], '-o', label='defender0')
    plt.plot(df['def1_x'], df['def1_y'], '-o', label='defender1')
    plt.plot(df['intr_x'], df['intr_y'], '-x', label='intruder')
    plt.scatter(df['intr_x'].iloc[-1], df['intr_y'].iloc[-1], c='red', label='final intruder')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.legend()
    plt.grid(True)
    out = 'plots/trajectories_demo.png'
    plt.savefig(out, dpi=150)
    print("[INFO] Saved trajectory plot to", out)
    plt.show()
