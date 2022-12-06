from marshmallow import Schema, fields


# Swagger Response Schema in UI
class IsAliveResponseSchema(Schema):
    message = fields.Bool(default=True)
    

    
class AtrialFibrillationResponseSchema(Schema):
    afib_percent = fields.Float(default=0.0)


class AtrialFibrillationRequestSchema(Schema):
    age       = fields.Integer(default=None)
    sex       = fields.String(default=None)
    height    = fields.Float(default=None)
    weight    = fields.Float(default=None)
    ritmi     = fields.Integer(default=None)
    I         = fields.Float(default=None)
    II        = fields.Float(default=None)
    III       = fields.Float(default=None)
    aVF       = fields.Float(default=None)
    aVR       = fields.Float(default=None)
    aVL       = fields.Float(default=None) 
    V1        = fields.Float(default=None)
    V2        = fields.Float(default=None)
    V3        = fields.Float(default=None) 
    V4        = fields.Float(default=None)
    V5        = fields.Float(default=None)
    V6        = fields.Float(default=None)
    


class AtrialFibrillationEcgSchema(Schema):
    I    =  fields.Float(default=None)
    II   =  fields.Float(default=None)
    III  =  fields.Float(default=None)
    aVF  =  fields.Float(default=None)
    aVR  =  fields.Float(default=None)
    aVL  =  fields.Float(default=None) 
    V1   =  fields.Float(default=None)
    V2   =  fields.Float(default=None)
    V3   =  fields.Float(default=None) 
    V4   =  fields.Float(default=None)
    V5   =  fields.Float(default=None)
    V6   =  fields.Float(default=None)

class AtrialFibrillationEcgResponseSchema(Schema):
    ecg = fields.List(fields.Nested(AtrialFibrillationEcgSchema))
    
