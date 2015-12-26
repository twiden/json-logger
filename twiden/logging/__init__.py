mport json
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
            d = kwargs.copy()
            d['_utc_timestamp'] = datetime.utcnow().isoformat()
            d['_component'] = self.name
            d['_level'] = self.level
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

