from flask import Flask

app = Flask(__name__)

def create_app(config=None):
    if config:
        app.config.from_object(config)
    return app