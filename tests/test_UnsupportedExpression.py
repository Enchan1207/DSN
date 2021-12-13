#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testUnsupportedExpression(TestCase):

    """ 対応していないDSNの変換 """

    @termdecorate
    def testUnsupportedExpression(self):
        """ 非対応のスキームに対する変換 """

        unsupported_dsn_schemes = [
            "ftp", "ftps", "ssh", "scp"
        ]
        dsns = [DSN(scheme) for scheme in unsupported_dsn_schemes]

        for dsn in dsns:
            with self.assertRaises(TypeError):
                DSNExpresser.urlexpr(dsn)

    def testActuallySupportedExpression(self):
        """ 対応していなさそうで実はしっかり対応してるスキームに対する変換 """

        actually_supported_urls = [
            "git+https://github.com/Enchan1207/python-dsn",
            "mysql+pymysql://user:pass@localhost:3306/path/to/db"
        ]

        for url in actually_supported_urls:
            dsn = DSN.parsefrom(url)
            dsn_url = DSNExpresser.urlexpr(dsn)
            self.assertEqual(url, dsn_url)
