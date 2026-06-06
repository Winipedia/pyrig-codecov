# pyrig-codecov

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

## What is pyrig-codecov

pyrig-codecov is a plugin for [pyrig](https://github.com/Winipedia/pyrig) that
integrates codecov into the testing workflow and enhances the code coverage reporting.

## Features

### Codecov Integration

Integrates codecov into the health check workflow, by uploading code coverage
reports to codecov

### Codecov Badge

Replaces the default code coverage badge with a codecov badge that shows the
code coverage percentage based on the uploaded codecov reports.

## Coverage Percentage

Increases the mimimum code coverage percentage to 100%.

## Usage

To use pyrig-codecov, add it as a developemnt dependency in your pyrig project
and run `pyrig mkroot` to generate the project structure. This will adjust all
necessary files.

```bash
uv add --group dev pyrig-codecov
uv run pyrig mkroot
```

If you are using pyrig with its Github workflows, you will need a
[Codecov](https://codecov.io) account and get an upload token there
and add this token as `CODECOV_TOKEN` to your repository secrets.
This is necessary for the codecov upload step in the health check workflow to work.
