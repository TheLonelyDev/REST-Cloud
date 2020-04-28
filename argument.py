from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

cls = get_driver(Provider.S3)

import inspect

for arg in inspect.getfullargspec(cls.create_container).args:
    if arg != "self":
        print(arg)


print([arg for arg in inspect.getfullargspec(cls.create_container).args if arg != "self"])