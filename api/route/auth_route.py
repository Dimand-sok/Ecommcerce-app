from api.utils.decorator import verify_authentication
from flask import Blueprint, make_response, request, abort, render_template
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_refresh_cookies,
    set_access_cookies,
    unset_jwt_cookies,
    get_jwt,
    jwt_required,
)

from dao import UserDao
from schema import UserSchema
from utils import validate_request


auth_route = Blueprint("auth_route",__name__, url_prefix="/api")


#Register route
@auth_route.route("/auth/register",methods=["POST"])
@validate_request(("UserSchema"))

def auth_register(user=None):
    with UserDao() as dao:
        _user = dao.add(user)
        user_json = dao.jsonify(UserSchema, _user)

    return make_response(user_json, 201)
 

#User Login route   
@auth_route.route("/auth/login",methods=["POST"])
@validate_request("UserSchema", only=["username", "password"])

def auth_login(user=None):
    with UserDao() as dao:
        _user = dao.get_by_username(user.get("username"))
        
        if not user:
            abort(404)
        
        if not _user.verify_password(user.get("password")):
            abort(401)
        
        user_json = dao.jsonify(UserSchema, _user)
        
        access_token = create_access_token(_user.username, additional_claims=user_json)
        refresh_toke = create_refresh_token(_user.username, additional_claims=user_json)
        
        response = make_response(user_json, 200)
        
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_toke)
    
    return response


#User logged route
@auth_route.route("/auth/logout", methods=["POST"])
@jwt_required()

def auth_logout():
    _user = get_jwt()
    response = make_response({"username": _user.get("username")})
    unset_jwt_cookies(response)
    
    return make_response(response, 200)



@auth_route.route("/test-auth", methods=["GET"])
@verify_authentication("admin")

def auth_test():
    return make_response({"message": "user logged in"}) 