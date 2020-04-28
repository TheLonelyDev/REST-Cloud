import inspect, libcloud

specs = []

# Get all module members of libcloud with inspect
for providerBase in inspect.getmembers(libcloud, inspect.ismodule):
    try:
        # Try to import the found module
        mdl = __import__("libcloud.%s" % providerBase[0], fromlist=["libcloud"])

        # Import fails = skip, we should not process this item

        # Try to address the two methods we need for creating the spec
        mdl.types.Provider
        mdl.providers.get_driver

        # If we cannot address the methods (aka they are missing)
        # Then this means that we are dealing with a module that is not a provider
        # = skip

    except:
        pass

print(specs)