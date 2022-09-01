from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask.signals import Namespace

from utils import get_notification
from route import *


app = Flask(
    __name__
)
    


all_routes = [route for name, route in globals().items() if isinstance(route, Blueprint)]
for route in all_routes:
    app.register_blueprint(route)

#create event using signal namespace required blinker package
namespace = Namespace()
notification_signal = namespace.signal("notification_signal")

@notification_signal.connect
def on_notification_signal(notif_type, **kwargs):
    notif = get_notification(type=notif_type)
    notif.send()


jwt = JWTManager(app)

def create_app(config=None):
    if config:
        app.config.from_object(config)
    return app