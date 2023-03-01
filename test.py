from sqlalchemy import create_engine, inspect, text
from sqlalchemy.dialects import registry as _registry

import sqlalchemy_pgspider

_registry.register(
    "pgspider.psycopg2", "sqlalchemy_pgspider.psycopg2", "PGSpiderDialect_psycopg2"
)

engine = create_engine("pgspider+psycopg2://pgspider:pgspider@/pgspiderdb?host=localhost&port=48131")
insp = inspect(engine)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 1}, {"x": 2, "y": 4}])
