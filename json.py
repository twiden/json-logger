import json
from datetime import datetime


def getLogger(name, **kwargs):
	return JsonLogger(name)


class JsonLogger(object):

	def __init__(self, name):
		import logging
		self.name = name
		logging.basicConfig(format='')
		logger = logging.getLogger(name)

		levels = ('info', 'warning', 'error', 'critical', 'log', 'exception')
		for l in levels:
			def log_func(data):
				if not isinstance(data, dict):
					raise TypeError('Log data must be dictionary')
				d = data.copy()
				d['_utc_timestamp'] = datetime.utcnow().isoformat()
				d['_component'] = self.name
				d['_level'] = l
				getattr(logger, l)(json.dumps(d))
			setattr(self, l, log_func)

