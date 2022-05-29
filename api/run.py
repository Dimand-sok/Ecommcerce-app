from app import create_app

from route import auth_route

current_app = create_app(dict())

current_app.register_blueprint(auth_route)

if __name__ == "__main__":
    current_app.run(debug=True, host='0.0.0.0', port=5000)