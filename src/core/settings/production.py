from .base import *

DEBUG = bool(int(os.getenv('DEBUG', True)))

try:
    from .local import *
except ImportError:
    pass
