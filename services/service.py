## /// buiness logic 

## data processing
from db.db import *
from services.validate_scheema import BaseSchema
import json
import pandas as pd
import pickle
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

class AtrialFibrillationServiceLayer:
    def __init__(self):
        self.col_AF = DB['AtrialFibrillationCollection']
        self.col_Person = DB['PersonCollection']
        self.inter_section_columns = ['V6','III','age','V2','V5','V4','weight','I','sex','II','V3','V1','aVR','height','ritmi','aVF','aVL']
    
    def Create_Schema(self, patient_schema):
        schema = BaseSchema()
        try:
            result = schema.load(patient_schema)
        except ValidationError as err:
             return json.dumps(err.messages)
         
        try:
            res = self.col.insert_one(patient_schema)
            return res.inserted_id
        except ValidationError as err:
            return "cannot insert patient schema"
        # call the collection from database
    
    def Get_Prediction(self, patient_schema):
        
        sub_test_data = {column: test_data[column] for column in self.inter_section_columns}
        test_df = pd.DataFrame(sub_test_data,index=[0])
        test_df['sex'] = test_df['sex'].apply(lambda x : 0 if x=='male' else 1)
        X_test = test_df.drop(columns='ritmi')
        y_test = test_df['ritmi']
        
          # load model
        modelfile = open(rf'weights\{str(len(inter_section_columns))}_feature_random_model.pkl','rb')
        model = pickle.load(modelfile)
        
             # do inference
        y_pred_prob = list(model.predict_proba(X_test)[0])

        prediction_string=f'{round(y_pred_prob[0],2)*100}% Normal (SR), {round(y_pred_prob[1],2)*100}% Atrial Fibrillation (AF), {round(y_pred_prob[2],2)*100}% All other arrhythmia (VA)'
            
        try:
            return prediction_string
        except Exception as e:
            return {'model_prediction':None}