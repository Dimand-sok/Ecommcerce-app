from model import CategoryModel
from .based_dao import BaseDAO

class CategoryDao(BaseDAO):
    def __init__(self, model=CategoryModel, close_on_exit=False):
        super().__init__(model, close_on_exit)
        
    def add(self, schema):
        model = self._model(schema)
        model.set_categoryName(schema.get("category_name"))
              
        self._session.add(model)
        self.commit()
        return model