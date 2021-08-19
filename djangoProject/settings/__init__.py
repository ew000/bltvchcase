from .base import *
import os
from decouple import config

if os.environ["ENV_NAME"] == 'Production':
    from .production import *
else:
    from .local import *