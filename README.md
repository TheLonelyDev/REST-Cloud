# REST-Cloud
This is an implementation of [Apache Libcloud](https://libcloud.apache.org/) using Flask to provide a REST API endpoint that you can interact with.

The endpoint/port of the app is 5000. Please expose this port on Docker.

## Documentation
This project was created with the intention of using Apache Libcloud's [documentation](https://libcloud.readthedocs.org/en/stable/) as a backbone. This means that said documentation can be used as a reference. We use the same parameter names, method names, configuration names, ... but everything is just wrapped inside a JSON object.

JSON structure (**please note that everything is case sensitive!**):
```json
{
    "method": "method",
    "driver": "driver",
    "provider": "provider",
    "data": {
        "parameter": "name"
    }
}
```

Example JSON object using the the following as a reference: [https://libcloud.readthedocs.io/en/stable/storage/api.html#libcloud.storage.base.StorageDriver.create_container](https://libcloud.readthedocs.io/en/stable/storage/api.html#libcloud.storage.base.StorageDriver.create_container)
```json
{
    "method": "create_container",
    "driver": "storage",
    "provider": "S3",
    "data": {
        "container_name": "my-test-container-22222"
    }
}
```

## Config
Please refer to the `sample-config.json` file and the Apache Libcloud [documentation](https://libcloud.readthedocs.org/en/stable/)  for more information.
