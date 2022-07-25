from distutils.debug import DEBUG

class DevConfigs:
    DEBUG= True
    PORT= 5000
    HOST = "0.0.0.0"
    SECRET_KEY="i3l_Y5AXQ)x7B7+S*OgjNd4-_0.+hHh?Gz?4gdyx#gRWjTFVdjw@-xZjy@Z-ij=Xc1B_yCWnmWm.mfH.?nJ8BU+egPJh:?#+kjC_!hDpU8Rva6Et+o6OSKIp5_*A#JG9"
    
    # JWT configuration
    JWT_TOKEN_LOCATION = ["cookies", "headers"]
    JWT_COOKIE_SECURE = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ERROR_MESSAGE_KEY = "errors"
    JWT_ACCESS_COOKIE_PATH = "/api/"
    JWT_REFRESH_COOKIE_PATH = "/api/refresh"
    JWT_REFRESH_CSRF_COOKIE_PATH = "/api/refresh"
    JWT_COOKIE_CSRF_PROTECT = False