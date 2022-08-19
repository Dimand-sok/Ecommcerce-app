from functools import wraps

from flask import abort, request, make_response
from stringcase import camelcase, snakecase
from marshmallow import ValidationError
from flask_jwt_extended import verify_jwt_in_request, get_jwt

from schema import *

def verify_authentication(role="customer"):
    """Custom decorator for validating request based on provided schemas
    param   schemas     String      string mashmallow schema class name
    param   options     Object      Mashmallow kwards options
    return decorator    Function    decorated function
    """

    def decorated(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            verify_jwt_in_request()

            current_user = get_jwt()

            if current_user.get("role") != role:
                abort(make_response({"message": "Invalid permission"}))

            print(current_user.get("role"), role)

            return function(*args, **kwargs)

        return wrapper

    return decorated

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
