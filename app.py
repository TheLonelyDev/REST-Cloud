import libcloud.security
from flask import Flask
from flask_restful_swagger import swagger
from flask_restplus import Api

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
