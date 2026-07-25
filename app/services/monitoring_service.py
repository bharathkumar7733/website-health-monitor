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
