# json-logger
Python JSON key-value logger

```python
from twiden import logging
logger = logging.getLogger(__name__)
logger.warning(what='Terrible danger!', how_much=100)

>>> {"_level": "warning", "what": "Terrible danger!", "_utc_timestamp": "2015-12-26T08:56:05.062067", "_component": "__main__"}
```

