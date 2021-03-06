import inspect
import json

import libcloud
import libcloud.security
from flask import Flask, request
from flask_restful_swagger import swagger
from flask_restplus import Api

# Config loader
config = {}
with open('./config.json') as file:
    config = json.load(file)

# Create Flask app
app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.0.1',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='REST Cloud API')

# Set debugging to true
app.run(debug=True)

# Set SSL verification to off
libcloud.security.VERIFY_SSL_CERT = False


# Spec builder
def build_specs():
    specs = []
    sorted_specs = {}

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

            sorted_specs[providerBase[0]] = []

            # Iterate over all the providers
            for provider in mdl.types.Provider.__dict__:
                # Check if the found member is private or not (prefixed with _)
                if provider[:1] != "_":
                    try:
                        # Get the driver
                        cls = mdl.providers.get_driver(getattr(mdl.types.Provider, provider))
                        sorted_specs[providerBase[0]][provider] = []

                        # List all methods
                        for method in inspect.getmembers(cls, inspect.isfunction):
                            # Set the current method to the method name (first entry of tupple)
                            method = method[0]

                            # Check if the found member is private or not (prefixed with _)
                            if method[:1] != "_":
                                # Create dictionary with info/data
                                spec = {
                                    "method": method,
                                    "driver": providerBase[0],
                                    "provider": provider,
                                    "data": {},
                                }

                                # Iterate over all the function parameter names and give them a blank value
                                for dataParam in [arg for arg in inspect.getfullargspec(getattr(cls, method)).args if
                                                  arg != "self"]:
                                    spec["data"][dataParam] = ""

                                # Add to the specs
                                specs.append(spec)
                                sorted_specs[providerBase[0]][provider].append(spec)
                    except:
                        pass
        except:
            pass

    return specs, sorted_specs


@app.route('/api', methods=['POST'])
def api_callback():
    try:
        # Read JSON object as a dictionary
        payload = request.json

        # Try to import the found module
        mdl = __import__("libcloud.%s" % payload["driver"], fromlist=["libcloud"])

        # Get the driver based on the provider
        cls = mdl.providers.get_driver(getattr(mdl.types.Provider, payload["provider"]))

        # Use the config option from the payload
        # If this is not present in the payload, use the default config
        driver = cls(**(payload["config"] if "config" in payload else config[payload["driver"]][payload["provider"]]))

        try:
            # Get the attribute/method from the driver by name
            # Invoke the method with the data from the payload
            # Finally return the representation of the object
            return getattr(driver, payload["method"])(**payload["data"]).__repr__(), 200, {
                'Access-Control-Allow-Origin': '*'}
        except Exception as e:
            # We got an error
            # Return the error type
            # Set the HTTP status code as 400
            return type(e).__name__, 400, {'Access-Control-Allow-Origin': '*'}
    except Exception as e:
        # We got an error
        # Return the error type
        # Set the HTTP status code as 400
        return type(e).__name__, 400, {'Access-Control-Allow-Origin': '*'}
