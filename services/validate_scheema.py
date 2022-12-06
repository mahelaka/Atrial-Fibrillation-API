from marshmallow import Schema, fields, ValidationError


class BaseSchema(Schema):
    age = fields.Integer(required=True)
    sex = fields.String(required=True)
    height = fields.Float(required=True)
    weight = fields.Float(required=True)
    ritmi =  fields.Integer(required=True)
    I = fields.Float(required=True)
    II = fields.Float(required=True)
    III = fields.Float(required=True)
    aVF =  fields.Float(required=True)
    aVR = fields.Float(required=True)
    aVL = fields.Float(required=True)
    V1 = fields.Float(required=True)
    V2 = fields.Float(required=True)
    V3 = fields.Float(required=True)
    V4 =  fields.Float(required=True)
    V5 =  fields.Float(required=True)
    V6  =  fields.Float(required=True)