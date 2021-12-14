#
# DSN
#
from __future__ import annotations

from typing import Any, List, Optional, Tuple, Type
from urllib.parse import urlparse
import re


class DSN():

    """DSNを表すクラス。

    DSNフォーマット: scheme://user:pass@host:port/path/to/transport
    最小構成: scheme://host/path

    Attributes:
        scheme   (str)           : スキーム
        user     (Optional[str]) : ユーザ名
        password (Optional[str]) : パスワード
        host     (Optional[str]) : ホスト名
        port     (Optional[int]) : ポート番号
        path     (str)           : パス
        params   (str)           : パラメータ
        query    (str)           : クエリ
        fragment (str)           : フラグメント
    """

    def __init__(self, scheme: str, user: Optional[str] = None,
                 password: Optional[str] = None,
                 host: Optional[str] = None,
                 port: Optional[int] = None,
                 path: str = "",
                 params: str = "",
                 query: str = "",
                 fragment: str = ""
                 ) -> None:
        """
        Raises:
            ValueError: 不正な引数が与えられた場合。
            TypeError: 引数の型が想定していたものと異なっていた場合。
        """

        # イニシャライザでは型チェックと基本的なバリデーションのみ行う

        expected_types: List[Tuple[Any, List[Type]]] = [
            (scheme, [str]),
            (user, [str, type(None)]),
            (password, [str, type(None)]),
            (host, [str, type(None)]),
            (port, [int, type(None)]),
            (path, [str]),
            (params, [str]),
            (query, [str]),
            (fragment, [str])
        ]
        validate_resultset = [type(arg) in types for arg, types in expected_types]
        if False in validate_resultset:
            raise TypeError("Invalid argument type")

        if not bool(re.match(r'^([a-z]|\.|\+|-)+$', scheme)):
            raise ValueError(f"invalid scheme: {scheme}")
        self.scheme: str = scheme

        self.user: Optional[str] = user
        self.password: Optional[str] = password
        self.host: Optional[str] = host

        if port is not None and (port < 0 or port > 65535):
            raise ValueError(f"Invalid port range (0-65536, {port})")
        self.port: Optional[int] = port

        self.path: str = path
        self.params: str = params
        self.query: str = query
        self.fragment: str = fragment

    def __str__(self) -> str:
        """DSNの文字列表現を返します。

        Returns:
            str: インスタンスの文字列表現。

        Note:
            DSNの文字列表現は正しいURLであることを保証しません。
            URLの形式で値を取得したい場合は `DSNExpresser.urlexpr()` を使用してください。
        """

        return f"{self.scheme}://{self.user or '(None)'}:{self.password or '(None)'}@{self.host}:{self.port or '(None)'}{self.path};{self.params}?{self.query}#{self.fragment}"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, DSN):
            return NotImplemented

        compare_param_names = [
            "scheme", "user", "password", "host", "port", "path", "query", "params", "fragment"
        ]
        compare_resultset = [getattr(self, key) == getattr(__o, key) for key in compare_param_names]

        return not False in compare_resultset

    @staticmethod
    def parsefrom(dsnstring: str) -> Optional[DSN]:
        """文字列からDSNインスタンスを生成します。

        Args:
            dsnstring(str): パース対象のDSN文字列。

        Returns:
            Optional[DSN]: パースして生成されたDSNインスタンス。生成に失敗した場合はNoneが返ります。

        """

        try:
            parsed_dsn = urlparse(dsnstring)

            return DSN(parsed_dsn.scheme,
                       parsed_dsn.username,
                       parsed_dsn.password,
                       parsed_dsn.hostname,
                       parsed_dsn.port,
                       parsed_dsn.path,
                       parsed_dsn.params,
                       parsed_dsn.query,
                       parsed_dsn.fragment)
        except (ValueError, TypeError):
            return None
