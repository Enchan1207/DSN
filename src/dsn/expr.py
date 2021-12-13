#
# URL表現生成
#
import re

from . import DSN
from .expressers import expressers


class DSNExpresser():

    """
    DSNのURL表現を生成するクラス。
    """

    @staticmethod
    def urlexpr(dsn: DSN) -> str:
        """DSNのURL表現を返します。

        Returns:
            str: インスタンスのURL表現。

        Raises:
            ValueError: DSNをURLとして表現できない場合。
            TypeError: DSNのスキームに対応する変換クラスが見つからなかった場合。
        """

        # スキームにあったexpresserを探す
        target_expressers = list(filter(lambda repr: re.match(
            re.compile(repr.__pattern__), dsn.scheme), expressers))
        if len(target_expressers) > 1:
            raise RuntimeError(
                f"pattern-matched multiple Expresser found: {','.join([n.__name__ for n in target_expressers])}")

        # expresserが見つからない場合はエラー
        if len(target_expressers) == 0:
            raise TypeError(f"No expresser found by scheme {dsn.scheme}")

        target_expresser = target_expressers[0]

        return target_expresser.urlexpr(dsn)
