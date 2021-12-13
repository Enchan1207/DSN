#
# HTTP DSN Expresser
#
from .. import DSN
from urllib.parse import urlunparse

from .base_expr import Base


class HTTPExpresser(Base):

    """ HTTP, HTTPSのExpresser """

    __pattern__: str = "^.*https*$"

    @staticmethod
    def urlexpr(dsn: DSN) -> str:

        # RFC 1738 3.3. HTTP
        # http://<host>:<port>/<path>?<searchpart>

        # 最低限hostは必要
        if dsn.host is None:
            raise ValueError("convert failed: HTTP requires host value, but None")

        # netlocを生成
        netloc_str = dsn.host
        if dsn.port is not None:
            netloc_str += f":{dsn.port}"

        # urlunparseで戻す
        return urlunparse((dsn.scheme, netloc_str, dsn.path, dsn.params, dsn.query, dsn.fragment))
