import time

import requests

from agent.collectors import get_device_info


API_URL = "http://127.0.0.1:8000/api/v1/devices/checkin"

HEARTBEAT_INTERVAL = 60


def send_checkin():
    device_info = get_device_info()

    try:
        response = requests.post(
            API_URL,
            json=device_info,
            timeout=10,
        )

        response.raise_for_status()

        print(
            f"[DevicePulse] Check-in successful: "
            f"{device_info['hostname']}"
        )

    except requests.RequestException as error:
        print(
            f"[DevicePulse] Check-in failed: {error}"
        )


def run_agent():
    print("[DevicePulse] Agent started.")
    print(
        f"[DevicePulse] Heartbeat interval: "
        f"{HEARTBEAT_INTERVAL}s"
    )

    try:
        while True:
            send_checkin()

            time.sleep(
                HEARTBEAT_INTERVAL
            )

    except KeyboardInterrupt:
        print("\n[DevicePulse] Agent stopped.")


if __name__ == "__main__":
    run_agent()