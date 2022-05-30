from app import create_app,DevConfigs

from route import auth_route

current_app = create_app(DevConfigs)

current_app.register_blueprint(auth_route)

if __name__ == "__main__":
    current_app.run(host=DevConfigs.HOST, port=DevConfigs.PORT)