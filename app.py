from flask import Flask, request
from flask_restplus import Resource, Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.0.1',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='REST Cloud API')
app.run(debug=True)
import libcloud.security

libcloud.security.VERIFY_SSL_CERT = False
