import threading
import time

from app.services.health_service import check_website
from app.services.servicenow_service import (
    create_incident,
    find_existing_incident,
)
from app.utils.logger import logger


monitoring_state = {
    "running": False,
    "url": None,
    "interval": None,
    "last_result": None,
}

stop_event = threading.Event()

def monitoring_loop(url: str, interval: int):
    while not stop_event.is_set():
        result = check_website(url)

        monitoring_state["last_result"] = result

        if result["status"] == "UP":
            logger.info(
                f"Continuous Monitor | Website: {url} | "
                f"Status: UP | HTTP Status: {result['status_code']}"
            )

        elif result["status"] == "DOWN":
            existing_incident = find_existing_incident(url)

            if existing_incident:
                logger.warning(
                    f"Continuous Monitor | Website: {url} | "
                    f"Status: DOWN | "
                    f"Incident: {existing_incident['incident_number']} | "
                    f"Action: Existing incident returned"
                )

            else:
                incident = create_incident(
                    short_description="Website Down",
                    description=f"{url} - {result['message']}"
                )

                logger.error(
                    f"Continuous Monitor | Website: {url} | "
                    f"Status: DOWN | "
                    f"Incident: {incident['incident_number']} | "
                    f"Action: New incident created"
                )

        stop_event.wait(interval)

    monitoring_state["running"] = False

def start_monitoring(url: str, interval: int):

    if monitoring_state["running"]:
        return False

    monitoring_state["running"] = True
    monitoring_state["url"] = url
    monitoring_state["interval"] = interval

    stop_event.clear()

    thread = threading.Thread(
        target=monitoring_loop,
        args=(url, interval),
        daemon=True
    )

    thread.start()

    return True


def stop_monitoring():

    stop_event.set()

    monitoring_state["running"] = False

    return True


def get_monitoring_status():

    return monitoring_state
