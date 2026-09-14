from datetime import datetime

from pydantic import BaseModel


class DeviceCheckin(BaseModel):
    hostname: str
    username: str

    operating_system: str
    os_version: str
    os_release: str
    architecture: str

    processor: str

    logical_cpus: int | None
    physical_cpus: int | None

    ram_gb: float
    disk_total_gb: float
    disk_free_gb: float

    ip_address: str
    uptime_hours: float


class Device(DeviceCheckin):
    last_checkin: datetime