from flask import Flask, Blueprint
from route import *

app = Flask(
    __name__,
    template_folder="/api/templates",
    )


all_routes = [route for name, route in globals().items() if isinstance(route, Blueprint)]
for route in all_routes:
    app.register_blueprint(route)


def create_app(config=None):
    if config:
        app.config.from_object(config)
    return app