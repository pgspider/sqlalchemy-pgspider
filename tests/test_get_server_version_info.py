from unittest.mock import MagicMock

import pytest

from sqlalchemy_pgspider.psycopg2 import PGSpiderDialect_psycopg2


def test_get_server_version_info():

    conn = MagicMock(exec_driver_sql=MagicMock(return_value=MagicMock(scalar=MagicMock())))

    ver = "PGSpider 15beta2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit"
    conn.exec_driver_sql().scalar.return_value = ver
    assert PGSpiderDialect_psycopg2._get_server_version_info(conn.self, conn) == (15, )

    conn.exec_driver_sql().scalar.return_value = "PGSpider 14.2, compiled by GCC"
    assert PGSpiderDialect_psycopg2._get_server_version_info(conn.self, conn) == (14, 2)

    with pytest.raises(Exception) as e:
        conn.exec_driver_sql().scalar.return_value="PostgreSQL 14.2, compiled by GCC"
        _ = PGSpiderDialect_psycopg2._get_server_version_info(conn.self, conn)

    assert "Could not determine version from string" in str(e.value)
