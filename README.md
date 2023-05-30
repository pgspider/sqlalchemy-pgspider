# sqlalchemy-pgspider

A SQLAlchemy dialect for [PGSpider](https://github.com/pgspider/pgspider).

## Overview

This is a module that allows you to connect to PGSpider using SQLAlchemy's PostgreSQL Dialect.

SQLAlchemy PostgreSQL Dialect uses the string obtained from pg_catalog.version() to determine whether it is PostgreSQL or not, and Postgres Dialect cannot be used to connect to PGSpider.

sqlalchemy-pgspider inherits PostgreSQL Dialect and overrides the part that checks version information, so that it can connect to PGSpider while retaining PostgreSQL Dialect functionality.

## System Requirements

The code here has been tested in the following environments.

* SQLALchemy 1.4.28 
* psycopg2 2.9.3
* Python 3.10.8
* pytest 7.2.2

It has been confirmed that almost all features supported by PostgreSQL's psycopg2 are available in SQLAlchemy 1.4.28.

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



## Basic Example

See test file [tests/test_create_engine.py](tests/test_create_engine.py)


## Testing 

### Requirements

* A PGSpider instance up and running
* pytest >= 6.2.1 installed on the testing machine

### Procedure

1. Change [conftest.py](tests/conftest.py) as appropriate
2. Run pytest
