from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException

from server.models import DeviceCheckin
from server.storage import load_devices, save_devices

app = FastAPI(
    title="DevicePulse API",
    description="Lightweight endpoint monitoring and inventory system.",
    version="1.0.0",
)


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
    return load_devices()


@app.get("/api/v1/devices/{hostname}")
def get_device(hostname: str):
    devices = load_devices()

    device = devices.get(hostname)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found.",
        )

    return device