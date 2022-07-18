
from flask import Blueprint, make_response, request, abort, render_template
from dao import UserDao


auth_route = Blueprint("auth_route",__name__, url_prefix="/api")



@auth_route.route("/auth/register",methods=["GET", "POST"])
def auth_register():
    print("working")
    if not request.is_json:
       abort(400)
    
    _user = request.get_json()
    
    with UserDao() as dao:
        user = dao.add(_user)
    return make_response({ "message":"Add successed"})
   
   
    
@auth_route.route("/login",methods=["GET", "POST"])

def login_user():
    return render_template("accounts/login.html")
    # return render_template("accounts/login.html")