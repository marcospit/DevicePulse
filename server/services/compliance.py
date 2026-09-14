MIN_RAM_GB = 8
MIN_FREE_DISK_GB = 20
MAX_UPTIME_HOURS = 24 * 30

SUPPORTED_OPERATING_SYSTEMS = {
    "Windows",
    "Linux",
    "Darwin",
}


def evaluate_compliance(device: dict) -> dict:
    checks = []
    issues = []
    unknown_checks = []

    # RAM
    ram_gb = device.get("ram_gb")

    if ram_gb is None:
        unknown_checks.append("ram")
    else:
        passed = ram_gb >= MIN_RAM_GB

        checks.append({
            "name": "minimum_ram",
            "passed": passed,
            "actual": ram_gb,
            "expected": f">= {MIN_RAM_GB} GB",
        })

        if not passed:
            issues.append(
                f"RAM below minimum requirement of {MIN_RAM_GB} GB"
            )

    # Free disk
    disk_free_gb = device.get("disk_free_gb")

    if disk_free_gb is None:
        unknown_checks.append("disk_free")
    else:
        passed = disk_free_gb >= MIN_FREE_DISK_GB

        checks.append({
            "name": "minimum_free_disk",
            "passed": passed,
            "actual": disk_free_gb,
            "expected": f">= {MIN_FREE_DISK_GB} GB",
        })

        if not passed:
            issues.append(
                f"Free disk space below {MIN_FREE_DISK_GB} GB"
            )

    # Uptime
    uptime_hours = device.get("uptime_hours")

    if uptime_hours is None:
        unknown_checks.append("uptime")
    else:
        passed = uptime_hours <= MAX_UPTIME_HOURS

        checks.append({
            "name": "maximum_uptime",
            "passed": passed,
            "actual": uptime_hours,
            "expected": f"<= {MAX_UPTIME_HOURS} hours",
        })

        if not passed:
            issues.append(
                "Device uptime exceeds 30 days"
            )

    # Operating System
    operating_system = device.get("operating_system")

    if not operating_system:
        unknown_checks.append("operating_system")
    else:
        passed = operating_system in SUPPORTED_OPERATING_SYSTEMS

        checks.append({
            "name": "supported_operating_system",
            "passed": passed,
            "actual": operating_system,
            "expected": sorted(SUPPORTED_OPERATING_SYSTEMS),
        })

        if not passed:
            issues.append(
                f"Unsupported operating system: {operating_system}"
            )

    if issues:
        compliance_status = "non_compliant"

    elif unknown_checks:
        compliance_status = "unknown"

    else:
        compliance_status = "compliant"

    return {
        "status": compliance_status,
        "checks": checks,
        "issues": issues,
        "unknown_checks": unknown_checks,
    }