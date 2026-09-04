from collections.abc import Mapping


def validate(data: Mapping[str, object], schema: Mapping[str, type]) -> list[str]:
    errors: list[str] = []
    for key, expected in schema.items():
        if key not in data:
            errors.append(f"missing: {key}")
        elif not isinstance(data[key], expected):
            errors.append(f"invalid type: {key}")
    return errors
