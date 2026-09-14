from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException

from server.models import DeviceCheckin
from server.storage import load_devices, save_devices
from server.services.compliance import evaluate_compliance
from server.services.device_status import get_device_status


app = FastAPI(
    title="DevicePulse API",
    description="Lightweight endpoint monitoring and inventory system.",
    version="0.3.0",
)


def enrich_device(device: dict) -> dict:
    device_data = device.copy()

    last_checkin = device_data.get("last_checkin")

    if last_checkin:
        device_data["status"] = get_device_status(
            last_checkin
        )
    else:
        device_data["status"] = "unknown"

    device_data["compliance"] = evaluate_compliance(
        device_data
    )

    return device_data


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "devicepulse-api",
    }


@app.post("/api/v1/devices/checkin")
def device_checkin(device: DeviceCheckin):
    devices = load_devices()

    device_data = device.model_dump()

    device_data["last_checkin"] = datetime.now(
        timezone.utc
    ).isoformat()

    devices[device.hostname] = device_data

    save_devices(devices)

    return {
        "message": "Device check-in received.",
        "hostname": device.hostname,
    }


@app.get("/api/v1/devices")
def list_devices():
    devices = load_devices()

    return [
        enrich_device(device)
        for device in devices.values()
    ]


@app.get("/api/v1/devices/{hostname}")
def get_device(hostname: str):
    devices = load_devices()

    device = devices.get(hostname)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail=f"Device '{hostname}' not found.",
        )

    return enrich_device(device)