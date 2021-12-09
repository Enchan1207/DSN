# python-dsn

## Overview

DSN(Data Source Name) utility for python.

## Installation

```sh
pip install git+https://github.com/Enchan1207/python-dsn
```

For `setup.cfg`:

```ini
install_requires=
    dsn @ git+https://github.com/Enchan1207/python-dsn
```

## Usage

```python
from dsn import DSN

# instantiate DSN from __init__
sample_dsn_full = DSN(
    "https", "user", "password", "example.com", 443, "/path/to/source")
sample_dsn_simple = DSN(
    "https", None, None, "example.com", 443, "/path/to/source")

# difference of URL representation and string representation
print("sample_dsn_full")
print(f"    string repr: {sample_dsn_full}")
print(f"    url    repr: {sample_dsn_full.url()}")

print("----")

print("sample_dsn_simple")
print(f"    string repr: {sample_dsn_simple}")
print(f"    url    repr: {sample_dsn_simple.url()}")

# instantiate DSN Object from string
url_str = "http://user:password@example.com:80/path/to/source/"
url_dsn = DSN.parsefrom(url_str)
assert(url_dsn is not None)

mysql_str = "mysql://user:pass@localhost:3306/test_database"
mysql_dsn = DSN.parsefrom(mysql_str)
assert(mysql_dsn is not None)

print(url_dsn.url())
print(mysql_dsn.url())
```

## License

This repository is published under [MIT License](LICENSE).
