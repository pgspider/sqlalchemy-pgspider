# sqlalchemy-pgspider-sample

I have confirmed that it works with Python3.10.8.

When running in a virtual environment, do the following
```
python3 -m venv
source venv/bin/activate 
```

Install packages.

```
pip intall -r requirements.txt 
```

Execute sample code.
```
python3 test.py
```

Change the arguments given to the `create_engine()` method in `test.py` as needed.

```
engine = create_engine("pgspider+psycopg2://pgspider:pgspider@/pgspiderdb?host=localhost&port=48131")
```

