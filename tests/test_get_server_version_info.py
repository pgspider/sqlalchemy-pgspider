from unittest.mock import MagicMock

import pytest

from sqlalchemy_pgspider.psycopg2 import PGSpiderDialect_psycopg2


def conn(str):
    mock = MagicMock(exec_driver_sql=MagicMock(return_value=MagicMock(scalar=MagicMock())))
    mock.exec_driver_sql().scalar.return_value = str
    return mock

@pytest.mark.parametrize(
    "pgspider_ver_str, result",
    [
        ( "PGSpider 15beta2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit", (15, ) ),
        ( "PGSpider 14.2, compiled by GCC", (14, 2) ),
        ( "PostgreSQL 15beta2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit", (15, )),
        ( "PostgreSQL 14.2, compiled by GCC", (14, 2) ),
        ( "EnterpriseDB 15beta2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit", (15, )),
        ( "EnterpriseDB 14.2, compiled by GCC", (14, 2) ),
    ]
)
def test_get_server_version_info(pgspider_ver_str, result):
    assert PGSpiderDialect_psycopg2._get_server_version_info(None, conn(pgspider_ver_str)) == result
