from schemacheck import validate


def test_valid():
    assert validate({"name": "medu", "age": 20}, {"name": str, "age": int}) == []


def test_errors():
    assert validate({"age": "20"}, {"name": str, "age": int}) == ["missing: name", "invalid type: age"]
