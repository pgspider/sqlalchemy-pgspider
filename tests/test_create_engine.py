import pytest
from sqlalchemy import create_engine, inspect


@pytest.mark.parametrize(
    "pgspider_protocol",
    [
        "pgspider",
        "pgspider+psycopg2",
    ]
)
def test_create_engine(settings, pgspider_protocol):
    engine = create_engine(f"{pgspider_protocol}://{settings['DBUSER']}:{settings['DBPASS']}@/{settings['DBNAME']}?host={settings['DBHOST']}&port={settings['DBPORT']}")
    inspect(engine)

@pytest.mark.parametrize(
    "otherdb_protocol",
    [
        "postgresql",
        "postgresql+psycopg2",
    ]
)
def test_create_engine_with_other_protocol(settings, otherdb_protocol):
    engine = create_engine(f"{otherdb_protocol}://{settings['DBUSER']}:{settings['DBPASS']}@/{settings['DBNAME']}?host={settings['DBHOST']}&port={settings['DBPORT']}")
    with pytest.raises(Exception) as e:
        inspect(engine)
    assert "Could not determine version from string" in str(e.value)
