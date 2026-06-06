# pyrig-codecov Documentation

<!-- security -->
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
<!-- tooling -->
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-codecov?style=social)](https://github.com/Winipedia/pyrig-codecov)
[![ContainerEngine](https://img.shields.io/badge/Container-Podman-A23CD6?logo=podman&logoColor=grey&colorA=0D1F3F&colorB=A23CD6)](https://podman.io)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
<!-- documentation -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://www.mkdocs.org)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-black?style=for-the-badge&logo=github&logoColor=white)](https://Winipedia.github.io/pyrig-codecov)
<!-- code-quality -->
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
<!-- project-info -->
[![ProgrammingLanguage](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-codecov)](https://github.com/Winipedia/pyrig-codecov/blob/main/LICENSE)
<!-- testing -->
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-codecov/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-codecov)
<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-codecov/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-codecov/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-codecov/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-codecov/actions/workflows/release.yml)

---

> A pyrig plugin that integrates codecov.

---

## What it does

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin that wires
[Codecov](https://codecov.io) into your project:

- Enforces **100% coverage** as the pass threshold.
- Generates `coverage.xml` alongside your normal test run.
- Adds a Codecov upload step to the CI health-check workflow.
- Adds `coverage.xml` to your version control ignore list.
- Adds a Codecov badge to your README.

No configuration required — installing the package as a development dependency
is the whole setup. Then regenerate your pyrig configs as usual.
The plugin's overrides are picked up automatically.

## Installation

```bash
uv add --group dev pyrig-codecov
uv run pyrig mkroot
```

## Setup

Two one-time steps on the repository side:

1. **Codecov Account** - Get an account on [codecov.io](https://codecov.io).
2. **Upload Token** - Get an upload token from Codecov
3. **Add token to repository secrets** - Add the token to your repository secrets
on GitHub as `CODECOV_TOKEN`

After that, every CI health check run uploads its coverage report to Codecov.

## How it works

The plugin subclasses two pyrig base classes:

- **`CoverageTester`** — overrides the coverage threshold, report format,
  badge URLs, and the auth token key.
- **`HealthCheckWorkflowConfigFile`** — appends a
  `codecov/codecov-action@main` step to the matrix health-check job
