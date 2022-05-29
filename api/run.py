from app import app as current_app

if __name__ == "__main__":
    current_app.run(debug=True, host='0.0.0.0', port=5000)