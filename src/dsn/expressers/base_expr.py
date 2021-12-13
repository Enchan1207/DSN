#
# Expresserのベースクラス
#

from __future__ import annotations

from typing import Set, Type

from .. import DSN


class __BaseExpresser:

    expressers: Set[Type[__BaseExpresser]] = set()
    __pattern__: str = ""

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()

        cls.expressers.add(cls)

    @staticmethod
    def urlexpr(dsn: DSN) -> str:
        return NotImplemented


Base = __BaseExpresser
