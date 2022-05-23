from flask import Blueprint, make_response

auth_route = Blueprint("auth_route",__name__, url_prefix="/api")

@auth_route.route("/")

def register_user():
    return make_response({"message": "Successfully World"})