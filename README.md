# guigen

Auto-generate GUI forms from Python function type hints. Define your function signature, and guigen creates a corresponding input form that collects parameters and invokes the function.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
make test

# Run the demo
python -c "from autogui import autogui, example; autogui(example)"
```

## How It Works

guigen inspects function annotations to dynamically build Qt-based input widgets:
- `int` parameters get spin boxes
- `str` parameters get text fields
- Additional types can be extended

## License

See LICENSE file.
