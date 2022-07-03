from flask import Blueprint, make_response,render_template

auth_route = Blueprint("auth_route",__name__, url_prefix="/api")

# @auth_route.route("/register",methods=["GET", "POST"])

# def register_user():
#     return render_template("register.html")
#     # return make_response({"message":"success"})
    
@auth_route.route("/login",methods=["GET", "POST"])

def login_user():
    return render_template("accounts/login.html")
    # return render_template("accounts/login.html")