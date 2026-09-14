import getpass
import platform
import socket
import time

import psutil


def get_ip_address() -> str:
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.error:
        return "unknown"


def get_uptime_hours() -> float:
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    return round(uptime_seconds / 3600, 2)


def get_device_info() -> dict:
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "logical_cpus": psutil.cpu_count(logical=True),
        "physical_cpus": psutil.cpu_count(logical=False),
        "ram_gb": round(memory.total / (1024 ** 3), 2),
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_free_gb": round(disk.free / (1024 ** 3), 2),
        "ip_address": get_ip_address(),
        "uptime_hours": get_uptime_hours(),
    }