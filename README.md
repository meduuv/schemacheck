# SchemaCheck

> Lightweight validation helpers for JSON-like Python data.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

SchemaCheck provides a deliberately small validation layer for dictionaries and other JSON-like Python structures.

## Features

- Required-key validation
- Type checks
- Nested field validation
- Clear validation errors
- Zero runtime dependencies
- Simple Python API

## Installation

```bash
pip install schemacheck
```

## Quick Start

```python
from schemacheck import validate

validate(
    {"name": "medu", "age": 20},
    {"name": str, "age": int},
)
```

## Use Cases

SchemaCheck is useful as a lightweight building block for configuration validation, API input checks, CLI configuration and small automation projects.

## Design

```text
JSON-like data
      ↓
 schema rules
      ↓
 validation
      ↓
 clear failure / success
```

The project intentionally avoids a large validation framework when simple structured checks are enough.

## Development

```bash
python -m pytest
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
