# Contributing Guidelines

Thank you for your interest in contributing to DataCleanse-Lite!

## Branching and Pull Requests
1. Create a branch from `main`.
2. Write your code and ensure all tests pass (`pytest`).
3. Ensure formatting and linting pass (`pre-commit run --all-files`).
4. Submit a Pull Request targeting `main`.

## Strict Conventional Commits
All commits **must** follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard. This repository uses `release-please` to automatically generate `CHANGELOG.md` and semantic version bumps based on commit messages.

### Format
`<type>(<optional scope>): <description>`

### Types
- `feat:` A new feature (triggers a MINOR version bump).
- `fix:` A bug fix (triggers a PATCH version bump).
- `feat!:` or `fix!:` A breaking change (triggers a MAJOR version bump).
- `docs:`, `chore:`, `style:`, `refactor:`, `test:` Non-releasing changes.

Example: `feat(pipeline): add support for parsing nested JSON structures`

## Automated Versioning
When a PR is merged into `main`, a Release PR (`chore: release x.y.z`) is automatically created or updated. When the Maintainer merges this Release PR, a Git tag is created, and a GitHub Release is published. Do not manually edit `CHANGELOG.md` or version numbers.