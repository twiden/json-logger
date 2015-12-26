# json-logger
Python JSON key-value logger

```python
from twiden import logging
logger = logging.getLogger(__name__)
logger.warning(what='Terrible danger!', how_much=100)

>>> {
    "what": "Terrible danger!",
	"how_much": 100,
	"_timestamp": "2015-12-26T09:04:14.891102"
	"_started": "2015-12-26T10:22:33.183410",
	"_uptime": "0:00:33.306972",
	"_level": "warning",
	"_pid": 11578,
	"_component": "__main__",
	"_ip_address": "192.168.1.10",
	"_hostname": "MacBook-Air.local",
}
```
