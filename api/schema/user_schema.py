from marshmallow import fields, validate
from .base_schema import Mixin


class UserSchema(Mixin):
    username = fields.String(required=True, validate=validate.Length(min=8, max=36))
    password = fields.String(
        required=True, validate=validate.Length(min=16, max=128), load_only=True
    )
    first_name = fields.String(required=True, validate=validate.Length(max=64))
    last_name = fields.String(required=True, validate=validate.Length(max=64))
    email = fields.Email(required=True)
    phone = fields.String(required=True, validate=validate.Length(min=10, max=12))