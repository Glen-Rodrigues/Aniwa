# Installation

This guide explains how to install Aniwa for both end users and contributors.

---

# Requirements

Aniwa currently requires:

- Python 3.10+
- pip
- virtual environment support recommended

Verify your Python version:

```bash
python --version
````

---

# Install from PyPI

Install the latest release from PyPI:

```bash
pip install aniwa
```

Verify installation:

```bash
aniwa --help
```

Upgrade Aniwa:

```bash
pip install --upgrade aniwa
```

---

# Install from Source

Clone the repository:

```bash
git clone https://github.com/ReginaldErzoah/Aniwa.git
```

Move into the project:

```bash
cd Aniwa
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv .venv
source .venv/Scripts/activate
```

## macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

Install project dependencies:

```bash
pip install -r requirements.txt
```

Install Aniwa locally:

```bash
pip install -e .
```

---

# Development Installation

Install development dependencies:

```bash
pip install pytest ruff build twine
```

Optional dependencies:

## YAML Config Support

```bash
pip install pyyaml
```

## TOML Support (Older Python Versions)

```bash
pip install tomli
```

---

# Verify Installation

Run:

```bash
aniwa --help
```

You should see:

```text
Aniwa - Universal dataset profiling and intelligence.
```

Test profiling:

```bash
aniwa examples/customers.csv
```

---

# Supported Platforms

Aniwa currently supports:

* Windows
* macOS
* Linux

---

# Recommended Development Tools

## Editors

Recommended editors:

* VS Code
* PyCharm
* Neovim

## Recommended VS Code Extensions

* Python
* Ruff
* Pylance
* GitLens
* Error Lens

---

# Dependency Overview

Core dependencies include:

* Typer
* Rich
* Polars
* Pydantic
* Jinja2
* OpenPyXL
* ReportLab

---

# Packaging System

Aniwa uses:

* setuptools
* pyproject.toml
* wheel

Build package:

```bash
python -m build
```

---

# Publishing

Upload to PyPI:

```bash
twine upload dist/*
```

---

# Common Installation Problems

## Python Not Found

Install Python from:

[https://python.org](https://python.org)

Ensure Python is added to PATH.

---

## Virtual Environment Activation Fails

On Windows PowerShell:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Missing Dependencies

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

# Recommended Setup Philosophy

Aniwa development should prioritize:

* isolated environments
* reproducible builds
* pinned dependencies
* automated testing
* lightweight local workflows

---

# Next Steps

Continue with:

* quickstart.md
* first-profile.md
* configuration.md

```
