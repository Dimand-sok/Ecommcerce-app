from flask import Blueprint, make_response,render_template

auth_route = Blueprint("auth_route",__name__, url_prefix="/api")

@auth_route.route("/")

def register_user():
    return render_template("login.html")
    # return make_response({"message":"success"})