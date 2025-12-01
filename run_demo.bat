@echo off
REM Edit Blocks path if needed:
set BLOCKS_PATH=C:\Users\sriram\Documents\AirSim\Blocks\WindowsNoEditor\Blocks.exe

if not exist "%BLOCKS_PATH%" (
  echo Blocks.exe not found at %BLOCKS_PATH%
  pause
  exit /b 1
)

echo Starting AirSim Blocks...
start "" "%BLOCKS_PATH%"
timeout /t 10 /nobreak

echo Activating venv and running demo...
call venv\Scripts\activate.bat
python sim_runner.py

echo Running visualization...
python visualize.py

pause
