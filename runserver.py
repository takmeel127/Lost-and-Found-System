import os
import webbrowser
import subprocess
import time

# Project root path
project_root = r"D:\PROJECT\lost_found_management_system"

# Virtual environment Python path
venv_python = r"D:\PROJECT\lost_found_management_system\venv\Scripts\python.exe"

# Change to project root
os.chdir(project_root)

# Start Django server using venv Python
subprocess.Popen([venv_python, "manage.py", "runserver"])

# Wait a bit for server to start
time.sleep(3)

# Open browser automatically
webbrowser.open("http://127.0.0.1:8000")