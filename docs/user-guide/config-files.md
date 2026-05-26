# Configuration

Aniwa supports configuration files to simplify reusable profiling workflows.

Configuration files allow users and teams to define default profiling behavior without repeatedly passing CLI arguments.

This improves:

- reproducibility
- developer experience
- automation
- team workflows
- CI/CD integration
- governance consistency

---

# Why Configuration Matters

Without configuration files, users must repeatedly type:

```bash
aniwa dataset.csv \
  --report html \
  --template dark \
  --mode deep \
  --include summary,statistics,insights
```

Configuration files solve this problem.

---

# Configuration Philosophy

Aniwa configuration is designed to be:

- lightweight
- human-readable
- reproducible
- extensible
- automation-friendly

---

# Supported Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| YAML | `.yaml`, `.yml` |
| TOML | `.toml` |
| JSON | `.json` |

---

# Automatic Discovery

Aniwa automatically searches for configuration files in the current working directory.

Search order:

1. `aniwa.yaml`
2. `aniwa.yml`
3. `aniwa.toml`
4. `aniwa.json`

---

# Example Automatic Usage

If a configuration file exists:

```bash
aniwa customers.csv
```

Aniwa automatically loads configuration values.

---

# Custom Configuration Files

Users may explicitly provide configuration files.

Example:

```bash
aniwa customers.csv \
  --config configs/production.yaml
```

---

# CLI Override Priority

Configuration priority order:

```text
CLI arguments
→ config file
→ defaults
```

This means CLI arguments always override configuration values.

---

# Example Override

Configuration file:

```yaml
mode: deep
```

CLI:

```bash
aniwa dataset.csv --mode fast
```

Final mode:

```text
fast
```

---

# Example YAML Configuration

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

# Example TOML Configuration

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

# Example JSON Configuration

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

# Current Supported Configuration Fields

Aniwa currently supports:

| Field | Purpose |
|---|---|
| mode | profiling mode |
| report.format | report type |
| report.template | report template |
| report.output_dir | output directory |
| sections.include | included sections |
| sections.exclude | excluded sections |

---

# Profiling Mode Configuration

Possible values:

- `fast`
- `deep`

Example:

```yaml
mode: deep
```

---

# Report Format Configuration

Possible values:

- `console`
- `json`
- `html`
- `markdown`
- `excel`
- `pdf`

Example:

```yaml
report:
  format: html
```

---

# Template Configuration

Supported templates:

- default
- clean
- compact
- enterprise
- dark

Example:

```yaml
report:
  template: enterprise
```

---

# Output Directory Configuration

Example:

```yaml
report:
  output_dir: reports/
```

Aniwa automatically generates report filenames.

Example generated output:

```text
reports/aniwa_report.html
```

---

# Section Configuration

Example:

```yaml
sections:
  include:
    - summary
    - statistics
```

---

# Include vs Exclude

Only one of the following should be used:

- `include`
- `exclude`

Incorrect:

```yaml
sections:
  include:
    - summary

  exclude:
    - charts
```

---

# Internal Configuration Flow

Internal loading flow:

```text
CLI
→ load_active_config()
→ get_flattened_config()
→ resolve settings
→ profile execution
```

---

# Configuration Discovery Logic

Discovery function:

```python
discover_config_file()
```

Responsibilities:

- search supported filenames
- detect available config
- return active config path

---

# Internal Config Flattening

Nested config structures are flattened internally.

Example:

```yaml
report:
  format: html
```

Becomes:

```python
{
    "report": "html"
}
```

This simplifies CLI integration.

---

# Configuration Validation

Aniwa validates configuration values before profiling begins.

Examples:

- invalid profiling mode
- unsupported report format
- invalid sections

---

# Example Invalid Config

```yaml
mode: ultra
```

Error:

```text
Invalid profiling mode: ultra
```

---

# Missing Configuration Files

Missing config files do not crash Aniwa.

Aniwa safely falls back to defaults.

---

# Invalid File Paths

Invalid explicit config paths raise errors.

Example:

```bash
aniwa dataset.csv --config missing.yaml
```

---

# TOML Support

Aniwa uses:

```python
tomllib
```

Fallback:

```python
tomli
```

for older Python versions.

---

# YAML Support

Aniwa uses:

```python
PyYAML
```

for YAML parsing.

---

# JSON Support

Aniwa uses Python's built-in:

```python
json
```

module.

---

# Configuration and CI/CD

Configuration files are especially useful in CI pipelines.

Example:

```bash
aniwa dataset.csv --config ci.yaml
```

Benefits:

- reproducibility
- consistent validation
- automated workflows

---

# Team Workflow Benefits

Configuration files improve:

- onboarding
- shared profiling standards
- governance consistency
- repeatability

---

# Governance Benefits

Configuration enables standardized profiling policies.

Example:

```yaml
sections:
  include:
    - quality
    - insights
```

Useful for:

- audits
- compliance
- governance pipelines

---

# Recommended Repository Structure

Example:

```text
configs/
├── development.yaml
├── production.yaml
├── governance.yaml
└── ci.yaml
```

---

# Environment-Specific Configurations

Future workflows may support:

| Environment | Example |
|---|---|
| development | fast mode |
| production | deep mode |
| governance | enterprise reports |
| CI | lightweight validation |

---

# Future Configuration Goals

Future plans include:

- environment inheritance
- profile presets
- user-level global configs
- remote configs
- validation schemas
- secrets integration

---

# Possible Future Architecture

Future architecture may evolve into:

```text
aniwa/config/
├── loaders/
├── validators/
├── schemas/
├── presets/
└── environments/
```

---

# Enterprise Configuration Vision

Future enterprise features may include:

- organization defaults
- governance policies
- centralized standards
- policy enforcement

---

# Plugin Configuration Vision

Future plugins may register config fields.

Example:

```yaml
plugins:
  observability:
    enabled: true
```

---

# Security Considerations

Configuration files may eventually include:

- database credentials
- cloud settings
- pipeline integrations

Future versions may support:

- encrypted configs
- secret managers
- environment variables

---

# Best Practices

---

## Keep Configs Version Controlled

Configuration files should be committed to repositories when appropriate.

---

## Separate Environments

Use separate configs for:

- development
- production
- CI/CD

---

## Prefer Explicitness

Avoid ambiguous configuration values.

---

# Common Mistakes

---

## Invalid Modes

Incorrect:

```yaml
mode: ultra
```

Correct:

```yaml
mode: deep
```

---

## Mixing Include and Exclude

Use only one.

---

## Unsupported Report Formats

Ensure formats match supported enums.

---

# Example Production Workflow

```bash
aniwa warehouse.csv \
  --config configs/production.yaml
```

---

# Example CI Workflow

```bash
aniwa dataset.csv \
  --config configs/ci.yaml
```

---

# Long-Term Vision

Configuration is foundational to Aniwa becoming:

- an enterprise platform
- a governance tool
- an observability system
- a programmable profiling engine

---

# Summary

Aniwa configuration provides:

- reproducibility
- automation
- workflow simplification
- governance consistency
- scalable profiling workflows

It is a critical foundation for long-term extensibility and enterprise adoption.

---

# Next Steps

Continue with:

- profiling-modes.md
- output-formats.md
- architecture-overview.md
- scalability-roadmap.md