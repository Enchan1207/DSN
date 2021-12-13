#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testMySQLExpression(TestCase):

    """ MySQL URLの変換 """

    @termdecorate
    def testExpression(self):
        """ 有効なDSNから MySQL URLに変換 """

        valid_dsn_strings = [
            "mysql://user:pass@localhost:3306/test_db?charset=UTF-8",
            "mysql://user:pass@127.0.0.1:3306/test_db",
            "mysql://user@127.0.0.1:3306/test_db",  # NOSONAR (sonarlintパスワード要求してくるのか…)
            "mysql://user:pass@127.0.0.1/test_db"  # ポート省略
        ]

        for dsn_str in valid_dsn_strings:
            dsn = DSN.parsefrom(dsn_str)
            dsn_url = DSNExpresser.urlexpr(dsn)
            self.assertEqual(dsn_str, dsn_url)

    @termdecorate
    def testInvalidExpression(self):
        """ 無効なDSNの変換テスト """

        invalid_dsns = [
            DSN("mysql", None, None, "localhost", 3306, "/path/to/db"),  # ログイン情報欠落
        ]
        for dsn in invalid_dsns:
            with self.assertRaises(ValueError):
                DSNExpresser.urlexpr(dsn)
