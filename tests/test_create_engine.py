import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine.url import URL


def url(drivername, settings):
    return URL.create(
        drivername = drivername,
        username = settings['DBUSER'],
        password = settings['DBPASS'],
        host = settings['DBHOST'],
        port = settings['DBPORT'],
        database = settings['DBNAME'],
    )

@pytest.mark.parametrize(
    "pgspider_drivername",
    [
        "pgspider",
        "pgspider+psycopg2",
    ]
)
def test_create_engine(settings, pgspider_drivername):
    engine = create_engine(url(pgspider_drivername, settings))
    print(url(pgspider_drivername, settings))
    inspect(engine)

@pytest.mark.parametrize(
    "otherdb_drivername",
    [
        "postgresql",
        "postgresql+psycopg2",
    ]
)
def test_create_engine_with_other_protocol(settings, otherdb_drivername):
    engine = create_engine(url(otherdb_drivername, settings))
    with pytest.raises(Exception) as e:
        inspect(engine)
    assert "Could not determine version from string" in str(e.value)
