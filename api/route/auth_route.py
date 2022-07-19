from flask import Blueprint, make_response, request, abort, render_template
from dao import UserDao
from schema import UserSchema
from utils import validate_request


auth_route = Blueprint("auth_route",__name__, url_prefix="/api")


@auth_route.route("/auth/register",methods=["POST", "GET"])
@validate_request(("UserSchema"))

def auth_register(user=None):
    print("Route working")
    
    with UserDao() as dao:
        _user = dao.add(user)
        
        user_json = dao.jsonify(UserSchema, _user)

    return make_response(user_json, 201)
 
    
@auth_route.route("/login",methods=["GET", "POST"])
def login_user():
    return render_template("accounts/login.html")
    # return render_template("accounts/login.html")