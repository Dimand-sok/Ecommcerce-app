from marshmallow import fields, validate
from .base_schema import Minxin

class CategorySchema(Minxin):
    category_name = fields.String(required=True, validate=validate.Length(min=8, max=128))
    category_desc = fields.String(required=False, validate=validate.Length(max=512))