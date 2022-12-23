import sys
import os
sys.path.insert(0,os.getcwd())
from flask import Flask, request, Response, jsonify
from flask_restful import Api
from db.db import *
from server.server import ApiIsAlive, AtrialFibrillationPredictApi, AtrialFibrillationPutApi, AtrialFibrillationDeleteApi
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
api = Api(app)

# Swagger plugin for docs
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Atrial Fibrillation Detection API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-docs/'  # URI to access UI of API Doc
})

docs = FlaskApiSpec(app)

api.add_resource(ApiIsAlive, '/health')
docs.register(ApiIsAlive)

api.add_resource(AtrialFibrillationPredictApi, '/predict_result')
docs.register(AtrialFibrillationPredictApi)

api.add_resource(AtrialFibrillationPutApi, '/update_patient_record')
docs.register(AtrialFibrillationPutApi)

api.add_resource(AtrialFibrillationDeleteApi, '/delete_patient_record')
docs.register(AtrialFibrillationDeleteApi)

if __name__ == '__main__':
    InitDB()
    app.run(port=5000, debug=True)
