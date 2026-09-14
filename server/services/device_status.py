from datetime import datetime, timezone


ONLINE_THRESHOLD_SECONDS = 120
WARNING_THRESHOLD_SECONDS = 600


def get_device_status(last_checkin: str) -> str:
    checkin_time = datetime.fromisoformat(last_checkin)

    if checkin_time.tzinfo is None:
        checkin_time = checkin_time.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)

    elapsed_seconds = (now - checkin_time).total_seconds()

    if elapsed_seconds <= ONLINE_THRESHOLD_SECONDS:
        return "online"

    if elapsed_seconds <= WARNING_THRESHOLD_SECONDS:
        return "warning"

    return "offline"