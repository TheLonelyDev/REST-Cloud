import inspect, libcloud

specs = []

# Get all module members of libcloud with inspect
for providerBase in inspect.getmembers(libcloud, inspect.ismodule):
    try:
        # Try to import the found module
        mdl = __import__("libcloud.%s" % providerBase[0], fromlist=["libcloud"])

        # Import fails = skip, we should not process this item

    except:
        pass

print(specs)