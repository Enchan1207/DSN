from typing import Optional


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

    scheme: str
    user: Optional[str]
    password: Optional[str]
    host: Optional[str]
    port: Optional[int]
    path: str
    params: str
    query: str
    fragment: str

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

    def __str__(self) -> str:
        """DSNの文字列表現を返します。

        Returns:
            str: インスタンスの文字列表現。

        Note:
            DSNの文字列表現は正しいURLであることを保証しません。
            URLの形式で値を取得したい場合は `DSN.url()` を使用してください。

        """

    def __eq__(self, __o: object) -> bool: ...

    @staticmethod
    def parsefrom(dsnstring: str) -> Optional[DSN]:
        """文字列からDSNインスタンスを生成します。

        Args:
            dsnstring(str): パース対象のDSN文字列。

        Returns:
            Optional[DSN]: パースして生成されたDSNインスタンス。生成に失敗した場合はNoneが返ります。

        """
