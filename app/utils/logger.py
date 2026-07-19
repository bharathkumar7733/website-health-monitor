import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# Configure logger
logging.basicConfig(
    filename=log_folder / "monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Logger is working!")
