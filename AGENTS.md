# Agent Guidelines for Daily Tools

## Commands
- **Run script**: `python rename_bulk.py`
- **Test single script**: `python -m py_compile rename_bulk.py` (syntax check)
- **Lint**: `python -m flake8 rename_bulk.py` (if flake8 installed)
- **Format**: `python -m black rename_bulk.py` (if black installed)

## Code Style
- **Imports**: Standard library first, then third-party. One import per line.
- **Naming**: snake_case for functions/variables, PascalCase for classes (if any).
- **Docstrings**: Use triple quotes for all functions explaining purpose.
- **Error handling**: Validate inputs early, provide clear error messages.
- **Structure**: Use `if __name__ == "__main__"` guard for executable scripts.
- **Types**: No type hints required (pure Python standard library).
- **Formatting**: 4-space indentation, lines under 80 characters preferred.