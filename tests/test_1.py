from square_database_structure import create_database_and_tables
from square_database_structure.main import global_list_create


def test_global_list_create():
    assert isinstance(global_list_create, list)
    for database in global_list_create:
        assert isinstance(database, dict)
        assert "database" in database
        assert isinstance(database["database"], str)
        assert "schemas" in database
        assert isinstance(database["schemas"], list)
        for schema in database["schemas"]:
            assert isinstance(schema, dict)
            assert "schema" in schema
            assert isinstance(schema["schema"], str)
            assert "base" in schema
            # todo: assert type here
            assert "data_to_insert" in schema
            assert isinstance(schema["data_to_insert"], list)
            # todo: assert type here
            assert "stored_procedures_and_functions" in schema
            assert isinstance(schema["stored_procedures_and_functions"], list)
            # todo: assert type here


def test_create_database_and_tables(db_credentials, fixture_create_database_and_tables):
    db_username = db_credentials["user"]
    db_password = db_credentials["password"]
    db_ip = db_credentials["host"]
    db_port = db_credentials["port"]

    assert (
        create_database_and_tables(
            db_username=db_username,
            db_password=db_password,
            db_ip=db_ip,
            db_port=db_port,
            drop_if_exists=True,
        )
        is None
    )
