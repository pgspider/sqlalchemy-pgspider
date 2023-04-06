from setuptools import setup, find_packages

setup(
    name="sqlalchemy_pgspider",
    version="0.1",
    author="TOSHIBA CORPORATION",
    description="A PGSpider dialect for SQLAlchemy",
    packages=['sqlalchemy_pgspider'],

    entry_points={
        "sqlalchemy.dialects": [
            'pgspider.psycopg2 = sqlalchemy_pgspider.psycopg2:PGSpiderDialect_psycopg2'
            ]
    }
)