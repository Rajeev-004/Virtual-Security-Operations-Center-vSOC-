"""Demo log collection and simple keyword-based threat detection."""
import asyncio
from datetime import datetime


async def collect_logs() -> list[str]:
    """Return sample events to demonstrate the monitoring workflow."""
    await asyncio.sleep(1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [
        f"{timestamp} - User login succeeded",
        f"{timestamp} - File accessed",
        f"{timestamp} - Threat detected: suspicious login attempt",
        f"{timestamp} - System scan completed",
        f"{timestamp} - Threat detected: unauthorized access attempt",
        f"{timestamp} - User logout succeeded",
    ]


def analyze_logs(logs: list[str]) -> list[str]:
    """Flag sample log lines containing the word 'threat'."""
    return [line for line in logs if "threat" in line.lower()]
