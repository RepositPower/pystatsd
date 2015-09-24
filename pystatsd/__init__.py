try:
    from rutils import setupLogging
    setupLogging()
except ImportError:
    pass

from .statsd import Client
from .server import Server

VERSION = (0, 1, 10)
