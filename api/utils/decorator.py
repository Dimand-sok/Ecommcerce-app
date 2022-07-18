from functools import wraps

from flask import abort, request
from stringcase import camelcase, snakecase
from marshmallow import ValidationError

from schema import *


def validate_request(*schemas, partial=False, **options):
    """Custom decorator for validating request based on provided schemas
    param   schemas     String      string mashmallow schema class name
    param   options     Object      Mashmallow kwards options
    return decorator    Function    decorated function
    """

    def decorated(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            if not request.is_json:
                abort(400)

            if not schemas:
                return function(*args, **kwargs)

            schema_objects = {}

            try:
                for klass in schemas:
                    if klass in globals().keys():
                        schema = globals()[klass]
                        value = schema(**options).load(
                            request.get_json(), partial=partial
                        )

                        schema_objects.update(
                            {snakecase(klass).replace("_schema", ""): value}
                        )

            except ValidationError as e:
                abort(400)

            return function(*args, **kwargs, **schema_objects)

        return wrapper

    return decorated
