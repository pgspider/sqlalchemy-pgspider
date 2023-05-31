from sqlalchemy import create_engine, inspect, text


def test_create_engine(settings):

    engine = create_engine(f"pgspider://{settings['DBUSER']}:{settings['DBPASS']}@/{settings['DBNAME']}?host={settings['DBHOST']}&port={settings['DBPORT']}")
    inspect(engine)

    engine = create_engine(f"pgspider+psycopg2://{settings['DBUSER']}:{settings['DBPASS']}@/{settings['DBNAME']}?host={settings['DBHOST']}&port={settings['DBPORT']}")
    inspect(engine)

    with engine.begin() as connection:
        connection.execute(text("DROP TABLE IF EXISTS some_table"))
        connection.execute(text("CREATE TABLE some_table (x int, y int)"))
        connection.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 1}, {"x": 2, "y": 4}])
        connection.execute(text("DROP TABLE some_table"))
