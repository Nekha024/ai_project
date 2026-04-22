# from utils.logger import get_logger

# logger = get_logger()
# logger.info("App started")

from loguru import logger

logger.add("logs/app.log", rotation="1 MB")

def get_logger():
    return logger