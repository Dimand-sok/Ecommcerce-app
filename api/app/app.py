from flask import Flask

app = Flask(__name__)

def create_app(config):
    print(app)
    return app