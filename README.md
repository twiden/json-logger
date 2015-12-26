# json-logger
Python JSON key-value logger

```python
from twiden import logging
logger = logging.getLogger(__name__)
logger.warning(what='Terrible danger!', how_much=100)

>>> {
	"_level": "warning",
	"what": "Terrible danger!",
	"_component": "__main__",
	"_ip_address": "192.168.1.10",
	"how_much": 100,
	"_hostname": "MacBook-Air.local",
	"_utc_timestamp": "2015-12-26T09:04:14.891102"
}
```
