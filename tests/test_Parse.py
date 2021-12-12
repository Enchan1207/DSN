#
# DSN文字列パーステスト
#
from typing import Any, List
from termdecorator import termdecorate
from unittest import TestCase
from src.dsn import DSN
from random import randint, choice


class testParse(TestCase):

    @termdecorate
    def testParseValidDSN(self):
        """ 有効なDSNのパース """

        # 有効なDSNを色々生成する
        schemes = ["http", "https", "ftp", "ftps", "sftp", "scp", "ssh", "git",
                   "git+https", "git+ssh", "smb"]
        port = lambda: randint(0, 65535)
        dsns = [DSN(choice(scheme), "user", "pass", "example.com", port(), "/path/to/content")
                for scheme in schemes]

        # URL表現を取得して、パースで逆変換できるか確認する
        url_reprs = [DSN.parsefrom(dsn.url()) for dsn in dsns]

        for (dsn, url_repr) in zip(dsns, url_reprs):
            self.assertTrue(dsn == url_repr)
