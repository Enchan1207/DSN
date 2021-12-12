#
# インスタンス生成テスト
#
from typing import Any, List
from termdecorator import termdecorate
from unittest import TestCase
from src.dsn import DSN


class testInstantiate(TestCase):

    @termdecorate
    def testGenerateInvalidInstance(self):
        """ 無効なインスタンスの生成 """

        invalid_initialize_args: List[List[Any]] = [
            [123],
            [None],
            ["http", 123, 123],
            ["ftp", "user", "pass", 123],
            ["scp", "user", "pass", "example.com", 114514],  # ポート番号範囲外
            ["ssh", "user", "pass", "example.com", 22, 123],
            ["ssh", "user", "pass", "example.com", 22, None]
        ]
        for args in invalid_initialize_args:
            print(f"generate with args: {','.join([str(n) for n in args])}")
            with self.assertRaises((TypeError, ValueError)):
                _ = DSN(*args)

    @termdecorate
    def testGenerateInstance(self):
        """ 有効なインスタンスの生成 """

        # スキームのみ指定
        schemes = ["http", "ftp", "scp", "smb", "git+https", "git", "ssh",
                   "sftp", "https", "mysql", "sqlite", "c++", "console.log"]
        for scheme in schemes:
            dsn_str = str(DSN(scheme))
            print(dsn_str)

    @termdecorate
    def testBoundaryValue(self):
        """ 境界値テスト """

        # ポート番号
        _ = DSN("http", None, None, None, 0, "")
        _ = DSN("http", None, None, None, 65535, "")
        with self.assertRaises(ValueError):
            _ = DSN("http", None, None, None, -1, "")
            _ = DSN("http", None, None, None, 65536, "")
