# pyrig-codecov

<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-codecov/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-codecov/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-codecov/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-codecov/actions/workflows/deploy.yml)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-codecov/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-codecov)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- code-quality -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityLinter](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-codecov?style=social)](https://github.com/Winipedia/pyrig-codecov)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://Winipedia.github.io/pyrig-codecov)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-codecov?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-codecov)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-codecov)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-codecov)](https://github.com/Winipedia/pyrig-codecov/blob/main/LICENSE)

---

> A pyrig plugin that integrates codecov.

---

## Overview

pyrig-codecov is a [pyrig](https://github.com/Winipedia/pyrig) plugin that
uploads your test coverage to [Codecov](https://codecov.io) and reports it on
your project.

## What it adds

- **Coverage upload** — a step in the CI health-check workflow that sends your
  coverage report to Codecov.
- **Coverage badge** — a Codecov badge showing your current coverage.
- **100% threshold** — raises the required coverage to 100%.

## Usage

```bash
uv add pyrig-codecov --dev
uv run pyrig sync
```

Uploading from CI requires a `CODECOV_TOKEN` repository secret — see the
documentation for the one-time setup.

## Documentation

Full documentation, including the auto-generated API reference, is available on
the [documentation site](https://Winipedia.github.io/pyrig-codecov).
