from sqlalchemy import Column,String, Integer, Boolean
from passlib.hash import sha256_crypt

from app.database import Based
from .base_model import baseModel


# class userModel(Based,baseModel):
#     __tablename__ = "user"
    
#     user_id = Column(String(32), nullable=False)
#     __user_name = Column(String(64), nullable=False)
#     __email_address = Column(String(128), nullable=False)
#     __password = Column(String(32), nullable=False)
#     first_name = Column(String(32))
#     last_name = Column(String(32))
#     gender = Column(String(16))
#     photo = Column(String(128))
#     address = Column(String(64))
#     country = Column(String(64))
#     city = Column(String(64))
#     district = Column(String(64))
#     commune = Column(String(64))
#     phone_number = Column(Integer)
#     active = Column(Boolean)
    
#     def __init__(self, schema):
#         if not isinstance(schema, dict):
#             raise ArgumentError("Schema should be a diction")

#         for key, value in schema.items():
#             if hasattr(self, key) and getattr(self, key) != value:
#                 setattr(self, key, value)
                
#     @property
#     def email_address(self):
#         # condiction
#         # security check 1
#         # security check 2
#         return self.__email

#     @email_address.setter
#     def email(self, email):
#         # condiction
#         # security check 1
#         # security check 2
#         self.__email = email


#     def set_password(self, password):
#         # condiction
#         # security check 1
#         # hash password before save
#         self.__password = password
    
    
    
    
class UserModel(Based, baseModel):
    __tablename__ = "user"
    __username = Column("username", String(36), nullable=False)
    __email = Column("email", String(128), nullable=False)
    __password = Column("password", String(256), nullable=False)
    first_name = Column(String(64))
    last_name = Column(String(64))
    phone = Column(String(12))

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        pass

    def set_email(self, email):

        # check permissions and other logic

        self.__email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        pass

    def set_username(self, username):
        self.__username = username

    @property
    def password(self):
        pass

    @password.setter
    def password(self, password):
        pass

    def set_password(self, password):
        self.__password = sha256_crypt.encrypt(password)

    def __init__(self, schema):
        for key, value in schema.items():
            if getattr(self, key) != value:
                setattr(self, key, value)