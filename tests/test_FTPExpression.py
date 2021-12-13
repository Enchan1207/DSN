#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testFTPExpression(TestCase):

    """ FTP URLの変換 """

    @termdecorate
    def testExpression(self):
        """ 有効なDSNからFTP URLに変換 """

        valid_dsn_strings = [
            "ftp://user:pass@localhost:21/path/to/dir",
            "sftp://user:pass@localhost:21/path/to/dir",
            "ftps://user:pass@localhost:21/path/to/dir",
            "ftp://user@localhost:21/path/to/dir",
        ]

        for dsn_str in valid_dsn_strings:
            dsn = DSN.parsefrom(dsn_str)
            dsn_url = DSNExpresser.urlexpr(dsn)
            self.assertEqual(dsn_str, dsn_url)

    @termdecorate
    def testInvalidExpression(self):
        """ 無効なDSNの変換テスト """

        invalid_dsns = [
            DSN("ftp"),  # ホスト無指定
            DSN("ftps", port=443)  # ポート指定のみ
        ]
        for dsn in invalid_dsns:
            with self.assertRaises(ValueError):
                DSNExpresser.urlexpr(dsn)
