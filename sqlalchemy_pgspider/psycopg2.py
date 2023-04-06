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
