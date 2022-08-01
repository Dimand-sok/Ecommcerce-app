
from flask import Blueprint, make_response, request, abort, render_template


from dao import CategoryDao
from schema import CategorySchema
from utils import validate_request


category_route = Blueprint("category_route",__name__, url_prefix="/api")

@category_route.route("/product/category", methods=["POST"])
@validate_request("CategorySchema")
def add_category(category=None):
   
    with CategoryDao() as dao:
        _category = dao.add(category)
        category_json = dao.jsonify(CategorySchema, _category)

    return make_response(category_json, 201)
    # return make_response({"message": "Category route worked"})
