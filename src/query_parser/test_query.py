import pytest

from .query import Query


class TestQuery:
    def test_query_get_value(self):
        query = Query()
        assert query.get_value() == 42
