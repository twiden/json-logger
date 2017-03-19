import json
import socket
import os
import time
import psutil
from datetime import datetime


def getLogger(name, **kwargs):
    return JsonLogger(name)


class JsonLogger(object):

    class Log(object):

        def __init__(self, logger, name, level):
            self.logger = logger
            self.name = name
            self.level = level

        def __call__(self, **kwargs):
            now = datetime.now()
            pid = os.getpid()
            pidcreated = datetime.fromtimestamp(psutil.Process(pid).create_time())
            d = kwargs.copy()

            for k, v in d.items():
                try:
                    json.dumps(v)
                except TypeError:
                    raise TypeError('Value for key {} is not JSON serializable'.format(k))

            d['_timestamp'] = datetime.utcnow().isoformat()
            d['_started'] = pidcreated.isoformat()
            d['_uptime'] = str(now - pidcreated)
            d['_component'] = self.name
            d['_level'] = self.level
            d['_pid'] = pid
            d['_hostname'] = socket.gethostname()
            d['_ip_address'] = socket.gethostbyname(d['_hostname'])

            self.logger(json.dumps(d))

    def __init__(self, name):
        import logging
        self.name = name
        logging.basicConfig(format='')
        self.logger = logging.getLogger(name)

        levels = ('info', 'warning', 'error', 'critical', 'exception')
        for level in levels:
            setattr(self, level, self.Log(getattr(self.logger, level), self.name, level))

    def setLevel(self, level):
        self.logger.setLevel(level)

