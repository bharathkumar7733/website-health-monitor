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
        # Loop body to be implemented
        stop_event.wait(interval)
    monitoring_state["running"] = False
