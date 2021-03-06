from settings_base import *

PORT = 9081

SERVER_NAME = 'http://victorpantoja.com'

LOGGING['root']['handlers'] = ['file']
LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'formatter': 'detailed',
    'filename': '/var/log/porfolio/app.log',
    'encoding': 'utf-8',
}

MEMCACHE = {
    'servers': ('wedding_plattform.3dpyc9.cfg.use1.cache.amazonaws.com:11211',),
    'socket_timeout': 1,
}
