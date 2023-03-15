import logging

logging.warning("Watch out!")  # Really watch out!

log_format = "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
formatter = logging.Formatter(log_format)
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("practice")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
