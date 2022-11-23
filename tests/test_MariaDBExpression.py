#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testMariaDBExpression(TestCase):

    """ MariaDB URLの変換 """

    @termdecorate
    def testExpression(self):
        """ 有効なDSNから MariaDB URLに変換 """

        valid_dsn_strings = [
            "mariadb://user:pass@localhost:3306/test_db?charset=UTF-8",
            "mariadb://user:pass@127.0.0.1:3306/test_db",
            "mariadb://user@127.0.0.1:3306/test_db",  # NOSONAR (sonarlintパスワード要求してくるのか…)
            "mariadb://user:pass@127.0.0.1/test_db"  # ポート省略
        ]

        for dsn_str in valid_dsn_strings:
            dsn = DSN.parsefrom(dsn_str)
            dsn_url = DSNExpresser.urlexpr(dsn)
            self.assertEqual(dsn_str, dsn_url)

    @termdecorate
    def testInvalidExpression(self):
        """ 無効なDSNの変換テスト """

        invalid_dsns = [
            DSN("mariadb", None, None, "localhost", 3306, "/path/to/db"),  # ログイン情報欠落
            DSN("mysql", None, None, "localhost", 3306, "/path/to/db"),  # 接続先間違えてますよ
        ]
        for dsn in invalid_dsns:
            with self.assertRaises((ValueError, TypeError)):
                DSNExpresser.urlexpr(dsn)
