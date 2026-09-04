# SchemaCheck

Lightweight validation helpers for JSON-like Python data.

## Features

- Required-key checks
- Type checks
- Nested field validation
- Clear validation errors
- Zero runtime dependencies

```python
from schemacheck import validate

validate({"name": "medu", "age": 20}, {"name": str, "age": int})
```

Development: `python -m pytest`

MIT licensed. Built by meduuv. https://guns.lol/meduu
