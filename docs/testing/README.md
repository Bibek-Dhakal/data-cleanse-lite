# Testing Strategy

We rely on `pytest` for unit and integration testing.

## Test Tiers

1. **Unit Tests:** Located in `tests/`. Covers pure functions in `transform.py` and `validate.py`.
2. **Integration Tests:** (Planned) End-to-end execution of `pipeline.py` against mocked file systems.

## Execution

Run the entire test suite with coverage:

```bash
pytest
```
