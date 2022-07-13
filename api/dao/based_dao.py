# pylint: disable=W0613
from datetime import datetime
from flask import abort
from sqlalchemy import and_
from stringcase import snakecase, camelcase

from app.database import session


class BaseDAO:
    """Database access object class"""

    _model = None
    _query = None
    _session = None

    def __init__(self, model=None, close_on_exit=False):
        """Initial database connect
        param:  db      BaseModel       SQLAlchemy database model
        param:  model   DatabaseModel   Database table model class
        """
        self._session = session
        self._close_on_exit = close_on_exit
        self.set_model(model)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            self._session.rollback()
        else:
            try:
                self._session.commit()
            except:
                self._session.rollback()
                raise
            finally:
                if self._close_on_exit:
                    self._session.close()

    def set_model(self, model):
        """Set database model
        param:  db  BaseModel   Database table model class
        """
        self._model = model
        self._query = self._session.query(self._model) if model else self._query

    def get_query(self, **expression):
        """Generate sql query
        param:  expression          SQL expression object. ex: {"id": 1}
        return: query               SQLAlchemy query class
        """

        return self._query.filter_by(**expression).order_by(self._model.id.desc())

    def get(self, id):
        """Get row by id"""

        query = self._query.filter(self._model.id == id)
        
        return query.one_or_none()

    def get_by_ids(self, ids, column_name=None, **kwargs):
        """Get row by id"""

        query = self._query.filter(
            self._model.id.in_(ids)
            if column_name is None
            else getattr(self._model, column_name).in_(ids)
        )

        pagination = kwargs.get("pagination", {})

        data = query.all() if not pagination else query.paginate(**pagination)

        return data

    def get_all(self, **kwargs):
        """Query data from database based on model

        param:  expression          SQL expression object. ex: {"id": 1}
        param:  pagination          SQLAlchemy pagination object. ex: {page: 1, per_page: 2}
        return: data
        """

        expr = kwargs.get("expression", {})

        expr = {
            (f"_UserModel__{key}" if key in ["username", "email"] else key): value
            for key, value in expr.items()
        }

        query = self.get_query(
            **{
                key: value
                for key, value in expr.items()
                if key not in ["date", "ids", "column", "_year"]
            }
        )

        # ids query

        if expr.get("ids"):
            query = query.filter(
                self._model.id.in_(expr.get("ids", []))
                if not expr.get("column")
                else getattr(self._model, expr.get("column")).in_(expr.get("ids"))
            )

        # year query
        years = expr.get("_year", "").split(":")

        start_year, end_year = (
            [int(year) for year in years] if len(years) == 2 else [0, 0]
        )

        if start_year > 0 and end_year > 0:
            query = query.filter(
                and_(
                    self._model.year >= int(start_year),
                    self._model.year <= int(end_year),
                )
            )

        # date query

        start_date, end_date = (
            expr.get("date").split("to")
            if len(expr.get("date", "").split("to")) == 2
            else [None, None]
        )

        if start_date and end_date is None:
            query = query.filter(
                self._model.create_date
                >= datetime.strptime(start_date.strip(), "%d-%m-%Y %H:%M:%S")
            )
        elif start_date is None and end_date:
            query = query.fiter(
                self._model.create_date
                <= datetime.strptime(end_date, "%d-%m-%Y %H:%M:%S")
            )
        elif start_date and end_date:
            query = query.filter(
                and_(
                    self._model.create_date
                    >= datetime.strptime(start_date.strip(), "%d-%m-%Y %H:%M:%S"),
                    self._model.create_date
                    <= datetime.strptime(end_date.strip(), "%d-%m-%Y %H:%M:%S"),
                )
            )

        pagination = kwargs.get("pagination", {})

        data = query.all() if not pagination else query.paginate(**pagination)

        return data

    def add(self, schema, commit=True):
        """add model to database
        param   schema  Dict    the valid load schema object
        return  model   Object  the database model object
        """
        model = self._model(schema)
        self._session.add(model)
        if commit:
            self._session.commit()
        return model

    def add_all(self, schemas):
        """Add all data to the database
        params: schemas     List    list of marshmallow schemas
        return  new_model   List    list of database model classes
        """
        models = [self._model(schema) for schema in schemas]
        self._session.add_all(models)
        self._session.flush()
        self._session.commit()
        return models

    def update(self, schema):
        """Update data in database
        param:  schema  Schema  Marshmallow schema
        return  model   database model
        """
        id = schema.get("id")
        model = self.get(id)
        if not model:
            abort(404)
        for k, v in schema.items():
            if isinstance(v, dict):
                k = f"{k}_id"
                v = v.get("id")
            if hasattr(model, k) and getattr(model, k) != v:
                setattr(model, k, v)
        self._session.commit()
        return model

    def delete(self, id):
        """Delete data from database
        param:  id   Integer row id
        return  id  Integer Deleted row id
        """
        model = self.get(id)
        if not model:
            return None
        self._session.delete(model)
        self._session.commit()
        return id

    def commit(self):
        """Commit current session"""

        self._session.commit()

    def close(self):
        """close current session"""

        self._session.close()

    def jsonify(self, schema, model, many=False, raise_error=True, **kwargs):
        """jsonify database object to json
        param:  schema               marshmallow mapped schema
        param:  modal                database object mapped model
        return: schema  JSON|List
        """

        if not model:
            abort(404)

        _schema = (
            schema(
                many=False,
                **{
                    key: value
                    for key, value in kwargs.items()
                    if key in ["only", "exclude"]
                },
            )
            if hasattr(model, "items")
            else schema(
                many=many,
                **{
                    key: value
                    for key, value in kwargs.items()
                    if key in ["only", "exclude"]
                },
            )
        )

        schema = _schema.dump(model)

        class_name = (
            snakecase(model[0].__class__.__name__)
            if isinstance(model, list)
            else snakecase(model.__class__.__name__)
        )

        name = camelcase(class_name.replace("_model", ""))

        data = {f"{name}s": schema} if isinstance(model, list) else schema

        if not schema:
            abort(404)

        return data
