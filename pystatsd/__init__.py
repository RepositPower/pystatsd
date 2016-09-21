import logging
zbxsend_logger = logging.getLogger('zbxsender')
zbxsend_logger.setLevel(logging.CRITICAL)

from .statsd import Client
from .server import Server

VERSION = (0, 2, 5)
