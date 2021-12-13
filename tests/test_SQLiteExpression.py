#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testSQLiteExpression(TestCase):

    """ SQLite URLの変換 """

    @termdecorate
    def testExpression(self):
        """ 有効なDSNから SQLite URLに変換 """

        valid_dsn_strings = [
            "sqlite:///path/to/db",
            "sqlite:///:memory:"
        ]

        for dsn_str in valid_dsn_strings:
            dsn = DSN.parsefrom(dsn_str)
            dsn_url = DSNExpresser.urlexpr(dsn)
            print(dsn_str)
            print(dsn_url)
            print("-----")
            self.assertEqual(dsn_str, dsn_url)

    @termdecorate
    def testInvalidExpression(self):
        """ 無効なDSNの変換テスト """

        invalid_dsns = [
            DSN("sqlite", host="example.com", path="/path/to/db"),  # ホスト情報は無効
            DSN("sqlite", path="")  # パス情報なし
        ]
        for dsn in invalid_dsns:
            with self.assertRaises(ValueError):
                DSNExpresser.urlexpr(dsn)
