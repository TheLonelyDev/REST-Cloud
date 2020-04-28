from libcloud.storage.providers import get_driver
from libcloud.storage.types import Provider
import inspect

cls = get_driver(Provider.S3)

for arg in inspect.getfullargspec(cls.create_container).args:
    if arg != "self":
        print(arg)

print([arg for arg in inspect.getfullargspec(cls.create_container).args if arg != "self"])
