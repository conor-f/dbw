# dbw

Personal Attempt at SQL Drag Racing


## Overview

The barest of efforts to make a functionally working SQL engine. Only rule is
that you can't research anything related to databases while working on it.


## Features

- [ ] CREATE DATABASE
- [ ] DROP DATABASE
- [ ] CREATE TABLE
- [ ] DROP TABLE
- [ ] INSERT INTO <table> VALUES <values>
- [ ] SELECT <values> FROM <table> WHERE <condition>
- [ ] DELETE FROM <table> WHERE <condition>


## Setup

```
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/entrypoint.py
```

## Naming

dbw is `ROT-11("SQL")` and is pronounced like the English letter "w".
