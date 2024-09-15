from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import declarative_base

from square_database_structure.square.public import global_string_schema_name

Base = declarative_base(metadata=MetaData(schema=global_string_schema_name))

data_to_insert = []


class Test(Base):
    __tablename__ = "test"

    test_id = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    test_text = Column(String, nullable=False)


class App(Base):
    __tablename__ = "app"

    app_id = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    app_name = Column(String, nullable=False, unique=True)


data_to_insert.append(App(app_name="square_admin"))
data_to_insert.append(App(app_name="square_wallet"))
data_to_insert.append(App(app_name="square_todo"))
