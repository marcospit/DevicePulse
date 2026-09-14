import requests

from agent.collectors import get_device_info


API_URL = "http://127.0.0.1:8000/api/v1/devices/checkin"


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


if __name__ == "__main__":
    send_checkin()