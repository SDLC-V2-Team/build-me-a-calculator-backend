# Calculator

A simple command-line calculator implemented in Python.

## Usage

```bash
python calculator.py "expression"
```

Examples:

- `python calculator.py "2 + 3"`
- `python calculator.py "10 - 4 * (2 + 1)"`
- `python calculator.py "15 / 3"`

## Development

Setup:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

## Notes

This implementation uses Python's built-in `eval` with restricted globals for simplicity. It supports basic arithmetic operators: `+`, `-`, `*`, `/`, and parentheses. For a more robust solution, consider using a parser.

## License

MIT
