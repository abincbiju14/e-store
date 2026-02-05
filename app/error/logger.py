import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "error.log")

# Create logs folder if not exists
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.ERROR)

# Prevent duplicate logs
if not logger.handlers:

    # File handler (append mode)
    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    file_handler.setLevel(logging.ERROR)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
