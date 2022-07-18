
from model import UserModel
from .based_dao import BaseDAO


class UserDao(BaseDAO):
    def __init__(self, model=UserModel, close_on_exit=False):
        super().__init__(model, close_on_exit)
        
    def add(self, schema):
        model = self._model(schema)
        model.set_email(schema.get("email"))
        model.set_username(schema.get("username"))
        model.set_password(schema.get("password"))
        
        self._session.add(model)
        self.commit()
        return model