import json
from pathlib import Path

DATA_FILE = Path("data/devices.json")


def initialize_storage() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")


def load_devices() -> dict:
    initialize_storage()

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_devices(devices: dict) -> None:
    initialize_storage()

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            devices,
            file,
            indent=4,
            ensure_ascii=False,
            default=str,
        )