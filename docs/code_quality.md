# Code Quality & Formatting

This project enforces formatting, import sorting, and linting via **Ruff**, and commit message validation via
**conventional-pre-commit**. Automated checks are triggered on `git commit` via pre-commit hooks.

## Environment Setup

Install and activate the hooks locally:

```bash
pip install -e .[dev]
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files
pre-commit run
# Format code
ruff format .

# Lint code and apply auto-fixes
ruff check . --fix
git commit -m "fix(urgent): bypass hook" --no-verify
```
