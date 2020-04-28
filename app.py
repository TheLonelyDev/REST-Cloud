import libcloud.security
from flask import Flask
from flask_restful_swagger import swagger
from flask_restplus import Api

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.0.1',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='REST Cloud API')
app.run(debug=True)

libcloud.security.VERIFY_SSL_CERT = False
