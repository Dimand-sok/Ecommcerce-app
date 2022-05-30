from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://{db_username}:{db_pwd}@db/{db_name}".format(
        db_username=environ.get("DB_USERNAME"),
        db_pwd=environ.get("DB_PASSWORD"),
        db_name=environ.get("DB_NAME"),
    )
)

session = scoped_session(sessionmaker(engine))
Based = declarative_base(name="ec_app")