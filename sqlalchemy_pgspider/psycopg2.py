# sqlalchemy-pgspider/psycopg2.py
# Copyright (C) 2023 Toshiba Corporation
#
# This module is for connecting to PGSpider with SQLAlchemy.
# SQLAlchemy: https://www.sqlalchemy.org/
# It is a subclass of PostgresDialcet and most of its functionality is 
# implemented in the parent class.
# 
# the MIT License: https://www.opensource.org/licenses/mit-license.php

import re

from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2


class PGSpiderDialect_psycopg2(PGDialect_psycopg2):
    supports_statement_cache = True

    def _get_server_version_info(self, connection):
        v = connection.exec_driver_sql("select pg_catalog.version()").scalar()
        m = re.match(
            r".*(?:PGSpider) "
            r"(\d+)\.?(\d+)?(?:\.(\d+))?(?:\.\d+)?(?:devel|beta)?",
            v,
        )
        if not m:
            raise AssertionError(
                "Could not determine version from string '%s'" % v
            )
        return tuple([int(x) for x in m.group(1, 2, 3) if x is not None])
