"""VSOC monitoring loop and shared dashboard state."""
import asyncio
import logging
from logging.handlers import RotatingFileHandler

import alerting
import incident_response
import log_management
import threat_intelligence

shared_state = {"logs": [], "threats": [], "alerts": []}


def setup_logging() -> logging.Logger:
    logger = logging.getLogger("VSOC")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        file_handler = RotatingFileHandler(
            "vsoc.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(console)
        logger.addHandler(file_handler)
    return logger


async def monitor_loop() -> None:
    """Continuously process simulated logs for dashboard demonstration."""
    logger = setup_logging()
    logger.info("VSOC monitoring system started.")
    while True:
        try:
            logs = await log_management.collect_logs()
            threats = log_management.analyze_logs(logs)
            alerts = []
            for threat in threats:
                enriched = threat_intelligence.enrich_threat(threat)
                alerts.append(alerting.send_alert(enriched))
                incident_response.respond_to_threat(enriched)

            # Keep the latest sample cycle visible on the dashboard.
            shared_state["logs"] = logs
            shared_state["threats"] = threats
            shared_state["alerts"] = alerts
            logger.info("Processed %d logs; detected %d potential threats.", len(logs), len(threats))
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("Error in VSOC monitoring loop.")
            await asyncio.sleep(5)


async def main() -> None:
    await monitor_loop()


if __name__ == "__main__":
    asyncio.run(main())
