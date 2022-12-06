#/// API calling function
from flask_restful import Resource, Api
from flask import jsonify, request
from db.db import *
from bson import json_util, ObjectId
import json
from services.service import AtrialFibrillationServiceLayer
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from server.schema.swagger_schema import IsAliveResponseSchema, AtrialFibrillationRequestSchema ,AtrialFibrillationResponseSchema, AtrialFibrillationEcgResponseSchema


# API Health Check
class ApiIsAlive(MethodResource, Resource):
        
    @doc(description='Atrial Fibrillation API.', tags=['Health Check'])
    @marshal_with(IsAliveResponseSchema)   
    def get(self):
        return jsonify({'alive' : True})

# Atrial Fibrillation API implementation
class AtrialFibrillationApi(MethodResource,Resource):
    
    @doc(description='Atrial Fibrillation API.', tags=['AFIB Detection Request'])
    @use_kwargs(AtrialFibrillationRequestSchema, location=('json'))
    @marshal_with(AtrialFibrillationResponseSchema)
    def post(self):
        print("heloo initialization")
        patient_data  = request.data ## get the json data
        print(patient_data)
        srv = AtrialFibrillationServiceLayer() # initialization the service layer
        
        res = srv.Create_Schema(patient_data) # create the schema
        
        
        predict_result= srv.Get_Predict_Result(patient_data) # get the result
        
        return jsonify({"predicted result":json.loads(json_util.dumps(predict_result)) , "status": 200})
    
    
    
    
    @doc(description='Atrial Fibrillation API.', tags=['ECG Get Data Request'])
    @marshal_with(AtrialFibrillationEcgResponseSchema)
    def get(self):
        ecg = []
        col = DB['EcgCollection']
        count = 0
        for e in col.find({}):
            ecg.append(e)
            count += 1
            if count == 100:
                break
        ecg_data = json.loads(json_util.dumps(ecg))
        return jsonify(ecg_data)