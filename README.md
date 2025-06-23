# Boilerplate Python Module

> **Boilerplate Python component** for the In.Plan (SCP) platform, implementing standard structure, CI, linting, testing, and documentation according to the [In.Plan SCP Component Development Guidelines](https://wiki.yandex.ru/scp/team/standarty-razrabotki-komponentov/).

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Development](#development)
7. [Testing](#testing)
8. [Linting & Type Checking](#linting--type-checking)
9. [CI / GitLab Pipeline](#ci--gitlab-pipeline)
10. [Contributing](#contributing)

---

## Overview

`boilerplate-python-component` is a template Python package designed as a starting point for all new components on the In.Plan (SCP) platform. It incorporates:

- **Clean structure** aligned with SCP standards
- **GitLab CI/CD** with protected branches and merge requests
- **Pre-commit hooks** (Black, isort, Flake8, mypy)
- **pytest** for unit and integration tests
- **YAML-based logging** configuration
- **Docs** folder for architecture diagrams and higher‑level documentation

Use this repository as a base to streamline onboarding of new features and ensure consistency across all SCP components.

## Features

- Python 3.10+ support
- Poetry-based dependency management
- Built‑in configuration loader (`Config` class)
- Example core functionality with dependency injection
- Logging setup via `logging.yml`
- CI pipeline (`.gitlab-ci.yml`)

## Prerequisites

- Git ≥2.x
- Python ≥3.10
- Poetry ≥1.5

## Installation

```bash
# Clone the repo
git clone git@gitlab.platform.in-plan.ru:scp/code/components/boilerplate-python-component.git
cd boilerplate-python-component

# Install dependencies
poetry install
```

## Usage

```python

```

## Development

1. Install dev dependencies:
   ```bash
   poetry install --with dev
   ```
2. Install pre-commit
   ```bash
   pre-commit install
   ```
3. Run pre-commit on all files:
   ```bash
   pre-commit run --all-files
   ```
4. Add your feature branch:
   ```bash
   git checkout -b feature/INPOPT-123-add-focus
   ```
5. Implement your changes, commit with `INPOPT-xxx:` prefix, and open MR against `dev` branch.

Detailed guidelines are available in the [SCP Component Standards Wiki](https://wiki.yandex.ru/scp/team/standarty-razrabotki-komponentov/).

## Testing

```bash
poetry run pytest tests/
```

Test data, mocks, and reference datasets are stored under `tests/` in JSON/CSV format to track changes over time.

## Linting & Type Checking
```bash
# Run all pre-commit hooks
git add . && pre-commit run
```

## CI / GitLab Pipeline

- **Lint stage**: runs pre-commit hooks on all files
- **Test stage**: runs pytest suite

See `.gitlab-ci.yml` for details and branch protection rules on `dev` and `main`.

## Contributing

1. Create a branch from `dev`.
2. Follow commit and branch-naming conventions:
   - Branch name: `feature/INPOPT-<task>-<short-desc>`
   - Commit message: `INPOPT-<task>: <description>`
3. Ensure all tests pass and lint checks are green.
4. Open a Merge Request targeting `dev`, referencing the task in the tracker.
