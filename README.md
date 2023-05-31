# sqlalchemy-pgspider

A [SQLAlchemy](https://www.sqlalchemy.org/) Dialect for [PGSpider](https://github.com/pgspider/pgspider).

## Overview

This is a module that allows you to connect to PGSpider using SQLAlchemy's PostgreSQL Dialect.

SQLAlchemy PostgreSQL Dialect uses the string obtained from pg_catalog.version() to determine whether it is PostgreSQL or not, and Postgres Dialect cannot be used to connect to PGSpider.

sqlalchemy-pgspider inherits PostgreSQL Dialect and overrides the part that checks version information, so that it can connect to PGSpider while retaining PostgreSQL Dialect functionality.

> **note**  
> Only psycopg2 DBAPI is supported.

## Requirements

* SQLALchemy 1.4.27 or higher 
* psycopg2 (or psycopg2-binary) 2.9.0 or higher
* Python 3.8 or higher

Almost all features supported by PostgreSQL's psycopg2 in SQLAlchemy 1.4.28 are available.  
Other versions have not been tested.

## Installation

Packages can be installed from either PyPI or GitHub.

Install package from PyPI.

```
pip install sqlalchemy-pgspider
```

from GitHub.

```
pip install git+https://github.com/pgspider/sqlalchemy-pgspider
```

## Usage

To connect to PGSpider with SQLAlchemy, the following URL pattern can be used:

```
pgspider://<username>:<password>@/<dbname>?host=<host>&port=<port>
```

Instead of the `pgspider:` protocol, you can also use `pgspier+psycopg2:`.  
The behaviour is the same whichever you use.

```
pgspider+psycopg2://<username>:<password>@/<dbname>?host=<host>&port=<port>
```

For more detailed usage, see the SQLAlchemy PostgreSQL psycopg2 documentation.  
Just change the protocol part of the URL pattern in the documentation from `postgresql+psycopg2` to `pgspider`(or `pgspider+psycopg2`) to work.


> SQLAlchemy 1.4 Documentation Dialects PostgreSQL - psycopg2  
> https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2  


## Sample code for use cases.

```python
engine = create_engine("pgspider://user:pass@/dbname?host=localhost&port=4813")

with engine.begin() as connection:
    connection.execute(text("CREATE TABLE some_table (x int, y int)"))
    connection.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 1}, {"x": 2, "y": 4}])
```

## Testing 

### Requirements

* A PGSpider instance up and running
* pytest >= 7.1.1 installed on the testing machine

### Procedure

1. Change [tests/conftest.py](tests/conftest.py) as appropriate
2. Run pytest
