import logging
from datetime import datetime
import os

LOG_FILE = "/var/log/systemsoft.log"

def setup_logger():
    if not os.path.exists("/var/log"):
        os.makedirs("/var/log", exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

def log_info(message: str):
    logging.info(message)

def log_error(message: str):
    logging.error(message)
