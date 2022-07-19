
from stringcase import camelcase, snakecase
from marshmallow import pre_load, post_dump, fields, Schema, EXCLUDE


class JsMixin(Schema):
    class Meta:
        unknown = EXCLUDE
        
    @pre_load
    def to_snakecase(self, data, **kwargs):
        """Convert object key from Camelcase to snakeCase """
        
        for field in data:
            if data[str(field)] == "":
                data[str(field)] = None
        
        return {
            snakecase(key): None if value == "" else value
            for key, value in data.items()
        }
        
    @post_dump
    def to_camelcase(self, data, **kwargs):
        """Convert object key from  snakeCase to Camelcase"""
        
        for field in data:
            if data[field] is None:
                data[field] = ""
            
        return {
            camelcase(key): str(value) if value is None else value
            for key, value in data.items()
        }
        
class Minxin(JsMixin):
    id = fields.Int()
    create_date = fields.DateTime("%d-%m-%Y %H:%M", dump_only=True)
    update_date = fields.DateTime("%d-%m-%Y %H:%M", dump_only=True)