#
#
#
from unittest import TestCase

from src.dsn import DSN, DSNExpresser
from termdecorator import termdecorate


class testHTTPExpression(TestCase):

    """ HTTP URLの変換 """

    @termdecorate
    def testExpression(self):
        """ 有効なDSNからHTTP URLに変換 """

        valid_dsn_strings = [
            "http://example.com",
            "https://example.com",
            "http://example.com:8080/",
            "http://example.com:8080/path/to/content",

            # 現時点ではこのコたちは失敗する
            "http://example.com:8080/path/to/content?chardet=UTF-8#article",
            "http://example.com:8080/path/to/content#article"
        ]

        for dsn_str in valid_dsn_strings:
            dsn = DSN.parsefrom(dsn_str)
            dsn_url = DSNExpresser.urlexpr(dsn)
            self.assertEqual(dsn_str, dsn_url)

    @termdecorate
    def testInvalidExpression(self):
        """ 無効なDSNの変換テスト """

        invalid_dsns = [
            DSN("http"),  # ホスト無指定
            DSN("https", port=443)  # ポート指定のみ
        ]
        for dsn in invalid_dsns:
            with self.assertRaises(ValueError):
                DSNExpresser.urlexpr(dsn)
