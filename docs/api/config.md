# Configuration API

Aniwa provides a flexible configuration system that enables:

- reproducible profiling workflows
- team-level consistency
- CI/CD integration
- automation
- scalable project configuration
- future enterprise extensibility

The configuration system allows users to define reusable defaults instead of repeatedly passing CLI options.

---

# Why Configuration Matters

Modern data workflows require:

- consistency
- reproducibility
- automation
- portability
- scalability

Without configuration systems:

- commands become repetitive
- pipelines become fragile
- team workflows become inconsistent
- CI systems become difficult to maintain

Aniwa solves this through project-level configuration support.

---

# Configuration Architecture

Current architecture:

```text
CLI
→ config discovery
→ config loading
→ config flattening
→ CLI override resolution
→ profiling execution
```

---

# Configuration Discovery

Aniwa automatically searches for configuration files in the current working directory.

Discovery order:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

First matching file is loaded.

---

# Supported Configuration Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| YAML | .yaml / .yml |
| TOML | .toml |
| JSON | .json |

---

# Configuration File Examples

---

## YAML

```yaml
mode: deep

report:
  format: html
  template: dark
  output_dir: reports/

sections:
  include:
    - summary
    - schema
    - statistics
    - insights
```

---

## TOML

```toml
mode = "deep"

[report]
format = "html"
template = "dark"
output_dir = "reports/"

[sections]
include = ["summary", "schema", "statistics", "insights"]
```

---

## JSON

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
      "schema",
      "statistics",
      "insights"
    ]
  }
}
```

---

# Internal Config Loader

Aniwa uses:

```python
load_config(file_path)
```

to load raw configuration data.

---

# Internal Loader Flow

```text
config path
→ extension detection
→ parser selection
→ validation
→ flattening
→ CLI merge
```

---

# Config Discovery API

Internal discovery:

```python
discover_config_file()
```

Searches the current directory for supported config files.

---

# Config Loading API

Internal loading:

```python
load_active_config(config_file)
```

Responsibilities:

- validate file existence
- parse configuration
- handle errors
- return flattened config

---

# Configuration Flattening

Nested config structures are flattened internally.

Example:

```yaml
report:
  format: html
```

becomes:

```python
{
    "report": "html"
}
```

This simplifies CLI integration.

---

# Flattening Function

Internal function:

```python
get_flattened_config()
```

Responsibilities:

- normalize structures
- simplify access
- validate values

---

# CLI Override System

Aniwa uses strict override priority:

```text
CLI arguments
→ configuration file
→ internal defaults
```

---

# Override Example

Config:

```yaml
mode: deep
```

CLI:

```bash
aniwa dataset.csv --mode fast
```

Final result:

```text
mode = fast
```

CLI always wins.

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
- markdown
- excel
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

# Supported Sections

Valid sections:

| Section |
|---|
| summary |
| schema |
| quality |
| statistics |
| insights |
| charts |

---

# Include vs Exclude

Aniwa does not allow:

```yaml
include
```

and

```yaml
exclude
```

simultaneously.

This avoids ambiguity.

---

# Validation System

Aniwa validates:

- report formats
- profiling modes
- section names
- template names
- configuration structure

---

# Invalid Config Example

```yaml
mode: ultra
```

Error:

```text
Invalid mode in config: ultra.
Use 'fast' or 'deep'.
```

---

# Missing Config Files

Missing config files do not crash Aniwa.

Behavior:

```text
Warning
→ continue with defaults
```

---

# Explicit Config Files

Users may explicitly provide config files.

Example:

```bash
aniwa dataset.csv --config team.yaml
```

---

# Multiple Config Workflows

Different projects may use different config files.

Example:

```bash
aniwa dataset.csv --config production.yaml
aniwa dataset.csv --config staging.yaml
aniwa dataset.csv --config local.yaml
```

---

# Team Workflow Benefits

Configuration files improve:

- consistency
- onboarding
- collaboration
- reproducibility

---

# CI/CD Benefits

Configurations simplify automation.

Example:

```bash
aniwa dataset.csv --config ci.yaml
```

---

# Enterprise Benefits

Enterprise systems require:

- predictable workflows
- centralized standards
- reproducible profiling
- governance consistency

Configurations make this possible.

---

# Internal Parser Architecture

Current parser selection:

```python
if suffix == ".json":
    ...

if suffix == ".toml":
    ...

if suffix in [".yaml", ".yml"]:
    ...
```

---

# YAML Support

Aniwa uses:

```python
yaml.safe_load()
```

Benefits:

- security
- simplicity
- compatibility

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

# JSON Support

Aniwa uses Python's built-in:

```python
json
```

module.

---

# Error Handling Philosophy

Aniwa prioritizes:

- helpful errors
- graceful degradation
- clear validation
- predictable behavior

---

# Internal Error Flow

```text
parse config
→ validate config
→ raise user-friendly errors
```

---

# Future Configuration Vision

Future improvements may include:

- global configs
- layered configs
- environment configs
- profile presets
- remote configs
- validation schemas

---

# Global Configuration Vision

Possible future behavior:

```text
~/.aniwa/config.yaml
```

for user-level defaults.

---

# Layered Config Vision

Future hierarchy:

```text
global config
→ project config
→ environment config
→ CLI overrides
```

---

# Environment Config Vision

Possible future support:

```text
aniwa.dev.yaml
aniwa.prod.yaml
aniwa.test.yaml
```

---

# Preset Systems

Future presets may support:

```yaml
preset: governance
```

or:

```yaml
preset: lightweight
```

---

# Schema Validation Vision

Future systems may use:

- Pydantic
- JSON Schema
- typed validation

for stricter configs.

---

# Remote Config Vision

Future systems may load configs from:

- Git repositories
- cloud storage
- governance systems
- API endpoints

---

# Enterprise Governance Vision

Future enterprise systems may centrally manage:

- profiling standards
- compliance settings
- reporting rules
- organizational policies

---

# Security Considerations

Configurations may eventually contain:

- database credentials
- API keys
- governance policies

Future systems should support:

- secrets management
- encrypted configs
- secure loading

---

# Best Practices

---

## Keep Configs Versioned

Store config files in Git repositories.

---

## Use Separate Configs Per Environment

Examples:

```text
local.yaml
ci.yaml
production.yaml
```

---

## Prefer Explicit Templates

Avoid relying on defaults in shared environments.

---

## Use Configs in CI/CD

Improves reproducibility.

---

# Common Mistakes

---

## Invalid Modes

Incorrect:

```yaml
mode: ultra
```

---

## Invalid Sections

Incorrect:

```yaml
include:
  - everything
```

---

## Mixing Include and Exclude

Incorrect:

```yaml
include:
  - summary

exclude:
  - statistics
```

---

# Long-Term Architectural Role

The configuration system is foundational to:

- automation
- enterprise adoption
- governance workflows
- reproducibility
- scalable profiling systems

---

# Summary

Aniwa's configuration API provides:

- automatic config discovery
- YAML/TOML/JSON support
- CLI override handling
- validation
- scalable workflows
- future extensibility

It transforms Aniwa from a simple CLI tool into a configurable profiling platform.

---

# Next Steps

Continue with:

- api/reporting.md
- api/profiler.md
- architecture/core-engine.md
- architecture/reporting-system.md