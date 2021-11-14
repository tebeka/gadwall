# gadwall - Command Line Client to duckdb

[gadwall](https://en.wikipedia.org/wiki/Gadwall) is a pure Python based command line to [duckdb](https://duckdb.org/)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Gadwall_%28Anas_strepera%29_female_and_male_dabbling.jpg/640px-Gadwall_%28Anas_strepera%29_female_and_male_dabbling.jpg)

image from [wikimedia](https://en.wikipedia.org/wiki/Gadwall#/media/File:Gadwall_(Anas_strepera)_female_and_male_dabbling.jpg)

## Usage

```
$ python -m gadwall stocks.ddb 
Welcome to the gadwall, a duckdb shell. Type help or ? to list commands.

duckdb> ?

Documented commands (type help <topic>):
========================================
db  help  quit  schema

Undocumented commands:
======================
EOF

duckdb> db
stocks.ddb
duckdb> schema
stocks
duckdb> schema stocks
0 date TIMESTAMP False None False
1 symbol VARCHAR False None False
2 open FLOAT False None False
3 high FLOAT False None False
4 low FLOAT False None False
5 close FLOAT False None False
6 adj_close FLOAT False None False
7 volume INTEGER False None False
duckdb> SELECT symbol, MAX(close) FROM stocks GROUP BY symbol;
GOOG 1827.989990234375
MSFT 231.64999389648438
ORCL 65.30000305175781
duckdb> quit
```
