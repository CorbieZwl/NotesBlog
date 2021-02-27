import logging
import os
from django.conf import settings

def create_logger(filename):
    filepath = os.path.join(settings.LOG_PATH,filename)
    logger = logging.getLogger(filename)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(filepath)
    # handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(fmt=formatter)
    logger.addHandler(handler)
    return logger