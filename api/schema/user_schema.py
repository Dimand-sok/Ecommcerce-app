from marshmallow import fields, validate
from .base_schema import Minxin


class UserSchema(Minxin):
    username = fields.String(required=True, validate=validate.Length(min=8, max=36))
    password = fields.String(
        required=True, validate=validate.Length(min=16, max=128), load_only=True
    )
    first_name = fields.String(required=True, validate=validate.Length(max=64))
    last_name = fields.String(required=True, validate=validate.Length(max=64))
    email = fields.Email(required=True)
    phone = fields.String(required=True, validate=validate.Length(min=10, max=12))
    
class UserCredentialSchema(UserSchema):
    new_password = fields.String(
        required=True, validate=validate.Length(min=16, max=128), load_only=True
    )
    otp = fields.String(validate=validate.Length(min=6, max=6), load_only=True)