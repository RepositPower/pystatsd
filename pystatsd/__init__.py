try:
    from rutils import setupLogging
    setupLogging()

    import logging
    zbxsend_logger = logging.getLogger('zbxsender')
    zbxsend_logger.setLevel(logging.CRITICAL)
except ImportError:
    pass

from .statsd import Client
from .server import Server

VERSION = (0, 1, 6)
