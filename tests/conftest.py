import os

import pytest


@pytest.fixture(scope="session")
def settings():
    return {
        "DBHOST": "localhost",
        "DBPORT": 4813,
        "DBUSER": "pgspider",
        "DBPASS": "pgspider",
        "DBNAME": "pgspiderdb",
    }