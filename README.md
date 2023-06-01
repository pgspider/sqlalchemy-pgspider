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
* psycopg2 (or psycopg2-binary) 2.9 or higher
* Python 3.7 or higher

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
pgspider+psycopg2://<username>:<password>@/<dbname>?host=<host>&port=<port>
```

Instead of the `pgspier+psycopg2:`, you can also use `pgspider:`.  
The behaviour is the same whichever you use.

```
pgspider://<username>:<password>@/<dbname>?host=<host>&port=<port>
```

For more detailed usage, see the SQLAlchemy PostgreSQL psycopg2 documentation.  
Just change the protocol part of the URL pattern in the documentation from `postgresql+psycopg2` to `pgspider`(or `pgspider+psycopg2`) to work.


> SQLAlchemy 1.4 Documentation Dialects PostgreSQL - psycopg2  
> https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2  


## Sample code for use cases.

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

engine = create_engine("pgspider://pgspider:pgspider@/pgspiderdb?host=localhost&port=4813")
Base.metadata.create_all(engine)

with Session(engine) as session:
    bea = User(name="Bea")
    eddy = User(name="Eddy")
    lily = User(name="Lily")
    session.add_all([bea, eddy, lily])
    session.commit()

session = Session(engine)
stmt = select(User).where(User.name=="Lily")
for user in session.scalars(stmt):
    print(user)
session.close()
    
Base.metadata.drop_all(engine)
```

## Testing 

### Requirements

* A PGSpider instance up and running
* pytest >= 7.1.1 installed on the testing machine

### Procedure

1. Change [tests/conftest.py](tests/conftest.py) as appropriate
2. Run pytest
