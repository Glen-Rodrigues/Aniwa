# Configuration

Aniwa supports reusable configuration files for simplifying profiling workflows.

Configuration files allow teams and developers to define default profiling behavior without repeatedly passing CLI arguments.

This improves:

- reproducibility
- developer experience
- automation
- CI/CD workflows
- consistency across teams

---

# Supported Configuration Formats

Aniwa currently supports:

- YAML
- TOML
- JSON

Supported filenames:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Automatic Configuration Discovery

Aniwa automatically searches the current working directory for configuration files.

Example:

```bash
aniwa examples/customers.csv
```

If a supported config file exists, Aniwa automatically loads it.

---

# Configuration Priority

Aniwa resolves configuration using the following priority order:

```text
CLI arguments > Config file > Defaults
```

This means command-line arguments always override configuration values.

---

# YAML Example

`aniwa.yaml`

```yaml
mode: deep

report:
  format: html
  template: dark
  output_dir: reports/

sections:
  include:
    - summary
    - statistics
    - insights
```

---

# TOML Example

`aniwa.toml`

```toml
mode = "deep"

[report]
format = "html"
template = "dark"
output_dir = "reports/"

[sections]
include = ["summary", "statistics", "insights"]
```

---

# JSON Example

`aniwa.json`

```json
{
  "mode": "deep",
  "report": {
    "format": "html",
    "template": "dark",
    "output_dir": "reports/"
  },
  "sections": {
    "include": [
      "summary",
      "statistics",
      "insights"
    ]
  }
}
```

---

# Using Custom Config Files

You can specify a custom config file using:

```bash
aniwa examples/customers.csv \
  --config examples/config_sample.yaml
```

This is useful for:

- multiple environments
- reusable presets
- testing workflows
- CI pipelines

---

# Supported Configuration Fields

---

## Profiling Mode

```yaml
mode: deep
```

Supported values:

- fast
- deep

---

## Report Format

```yaml
report:
  format: html
```

Supported values:

- console
- json
- html
- excel
- markdown
- pdf

---

## Report Template

```yaml
report:
  template: dark
```

Supported values:

- default
- clean
- compact
- enterprise
- dark

---

## Output Directory

```yaml
report:
  output_dir: reports/
```

Aniwa automatically:

- creates directories
- generates filenames
- applies extensions

---

## Included Sections

```yaml
sections:
  include:
    - summary
    - statistics
```

---

## Excluded Sections

```yaml
sections:
  exclude:
    - charts
```

---

# CLI Override Examples

---

## Override Mode

Config:

```yaml
mode: deep
```

CLI:

```bash
aniwa dataset.csv --mode fast
```

Result:

```text
fast mode is used
```

---

## Override Template

Config:

```yaml
report:
  template: dark
```

CLI:

```bash
aniwa dataset.csv --template enterprise
```

Result:

```text
enterprise template is used
```

---

# Internal Configuration Flow

Aniwa internally performs:

1. config discovery
2. config parsing
3. validation
4. flattening
5. merging with CLI arguments
6. final runtime resolution

---

# Configuration Architecture

Configuration handling is primarily implemented in:

```text
aniwa/config.py
aniwa/config_loader.py
aniwa/cli.py
```

Responsibilities:

---

## config_loader.py

Responsible for:

- reading YAML
- reading TOML
- reading JSON
- parsing config structures
- flattening nested config values

---

## cli.py

Responsible for:

- discovering config files
- loading configs
- merging CLI overrides
- validating runtime configuration

---

# Config Validation

Aniwa validates:

- report format
- profiling mode
- report sections
- template names

Invalid configs raise helpful errors.

Example:

```text
Invalid mode in config: ultra
```

---

# Missing Config Files

Missing config files do not crash Aniwa.

Example:

```text
Warning: Configuration file not found.
Using defaults.
```

---

# Recommended Workflow

Recommended project setup:

```text
project/
├── datasets/
├── reports/
├── aniwa.yaml
```

Example:

```yaml
mode: deep

report:
  format: html
  template: enterprise
  output_dir: reports/
```

Then simply run:

```bash
aniwa datasets/customers.csv
```

---

# CI/CD Example

Example GitHub Actions workflow:

```yaml
- name: Run Aniwa
  run: |
    aniwa datasets/customers.csv
```

Since config is auto-discovered, workflows remain clean and reproducible.

---

# Future Configuration Roadmap

Future planned features include:

- environment configs
- user-level configs
- global configs
- remote configs
- validation schemas
- project presets
- profile inheritance
- encrypted configs
- plugin configs

---

# Design Philosophy

Aniwa configuration is designed to be:

- lightweight
- explicit
- reproducible
- automation-friendly
- developer-first

---

# Best Practices

Recommended practices:

- commit config files to repositories
- standardize team presets
- separate environment configs
- use CLI overrides sparingly
- keep configs minimal and readable

---

# Next Steps

Continue with:

- examples.md
- cli-reference.md
- report-formats.md
- profiling-modes.md