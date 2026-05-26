# Configuration System Architecture

The configuration system is one of the most important foundations for making Aniwa production-ready.

It transforms Aniwa from:

```text
a standalone CLI tool
```

into:

```text
a reusable, automatable, team-friendly profiling platform
```

---

# Purpose of the Configuration System

The configuration system exists to:

- simplify repeated workflows
- improve reproducibility
- standardize profiling behavior
- support CI/CD pipelines
- improve developer experience
- enable team-wide conventions
- prepare Aniwa for enterprise-scale workflows

---

# Why Configuration Matters

Without configuration files, users repeatedly pass CLI arguments:

```bash
aniwa customers.csv \
  --mode deep \
  --report html \
  --template dark \
  --include summary,statistics,insights
```

This becomes:

- repetitive
- error-prone
- difficult to automate
- difficult to standardize across teams

---

# Configuration Philosophy

Aniwa configuration is designed to be:

- simple
- readable
- portable
- extensible
- automation-friendly
- deterministic

---

# Current Supported Config Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| YAML | `.yaml`, `.yml` |
| TOML | `.toml` |
| JSON | `.json` |

---

# Why Multiple Config Formats Matter

Different ecosystems prefer different formats.

Examples:

| Ecosystem | Preferred Format |
|---|---|
| Python | TOML |
| DevOps | YAML |
| APIs | JSON |

Supporting all three improves adoption.

---

# Current Config Discovery System

Aniwa automatically searches for configuration files in the current working directory.

Search order:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Discovery Flow

```text
CLI starts
→ search current directory
→ find supported config
→ load config
→ flatten config
→ apply defaults
→ override with CLI args
```

---

# Current Config Architecture

Location:

```text
aniwa/config.py
```

---

# High-Level Architecture

```text
config file
→ parser
→ normalized dictionary
→ flattened config
→ CLI resolution
→ runtime behavior
```

---

# Why Flattened Configs Matter

Different config formats may have nested structures.

Example YAML:

```yaml
report:
  format: html
  template: dark
```

Flattened internally into:

```python
{
    "report": "html",
    "template": "dark"
}
```

This simplifies runtime resolution.

---

# Current Core Functions

Current major configuration functions include:

| Function | Purpose |
|---|---|
| `load_config()` | Loads raw config |
| `_read_config()` | Parses file by extension |
| `get_flattened_config()` | Normalizes config |
| `discover_config_file()` | Auto-discovers config |
| `load_active_config()` | Loads runtime config |

---

# Current Parsing System

---

## JSON Parsing

Uses:

```python
json.load()
```

---

## TOML Parsing

Uses:

```python
tomllib
```

Fallback:

```python
tomli
```

for older Python versions.

---

## YAML Parsing

Uses:

```python
yaml.safe_load()
```

via:

```text
PyYAML
```

---

# Why Safe Parsing Matters

Unsafe parsing can create:

- security risks
- code execution vulnerabilities
- injection problems

Using safe loaders is critical.

---

# Current Config Schema

Current supported configuration sections:

```yaml
mode:
report:
sections:
```

---

# Current Supported Settings

---

## Profiling Mode

```yaml
mode: deep
```

Supported:

| Value |
|---|
| fast |
| deep |

---

## Report Configuration

```yaml
report:
  format: html
  template: dark
  output_dir: reports/
```

---

## Section Configuration

```yaml
sections:
  include:
    - summary
    - statistics
```

---

# Current Supported Sections

| Section |
|---|
| summary |
| schema |
| quality |
| statistics |
| insights |
| charts |

---

# Configuration Resolution Priority

Aniwa uses:

```text
CLI arguments > config file > defaults
```

---

# Why This Priority Matters

Users expect:

- config files to provide defaults
- CLI arguments to override configs

This is standard behavior in mature tooling.

---

# Example Resolution

Config:

```yaml
mode: deep
```

CLI:

```bash
aniwa customers.csv --mode fast
```

Final runtime behavior:

```text
fast
```

because CLI overrides config.

---

# Runtime Resolution Architecture

```text
defaults
→ config values
→ CLI overrides
→ resolved runtime settings
```

---

# Why Runtime Resolution Matters

This enables:

- flexible workflows
- reproducibility
- team standards
- user customization

---

# Current CLI Integration

The CLI integrates configuration using:

```python
load_active_config()
```

---

# Current CLI Flow

```text
start CLI
→ discover config
→ parse config
→ validate config
→ merge CLI overrides
→ execute profiling
```

---

# Configuration Validation

Aniwa validates:

- profiling mode
- report format
- section names

---

# Why Validation Matters

Validation prevents:

- silent failures
- invalid runtime states
- broken reports
- inconsistent behavior

---

# Example Validation Error

```text
Invalid mode in config: ultra
Use 'fast' or 'deep'.
```

---

# Current Error Handling Philosophy

Configuration errors should be:

- explicit
- readable
- actionable
- non-cryptic

---

# Missing Config Philosophy

Missing config files should NEVER crash Aniwa.

Instead:

```text
fallback to defaults
```

---

# Why Graceful Failure Matters

Graceful failure improves:

- reliability
- usability
- developer trust

---

# Output Management Integration

Configuration integrates with:

```text
--output
--output-dir
```

systems.

---

# Current Output Resolution System

Aniwa supports:

```yaml
report:
  output_dir: reports/
```

---

# Output Resolution Flow

```text
config output_dir
→ generate filename
→ apply extension
→ create directories
→ render report
```

---

# Automatic Directory Creation

Aniwa automatically creates missing directories.

Example:

```yaml
output_dir: reports/profiles/
```

If missing:

```text
directories are created automatically
```

---

# Why Automatic Directories Matter

This improves:

- CI/CD integration
- automation
- usability
- developer experience

---

# Current Default Filenames

| Report Type | Default Filename |
|---|---|
| JSON | aniwa_report.json |
| HTML | aniwa_report.html |
| Excel | aniwa_report.xlsx |
| Markdown | aniwa_report.md |
| PDF | aniwa_report.pdf |

---

# Config + Templates Integration

Configs can define:

```yaml
template: dark
```

for HTML/PDF rendering.

---

# Current Template System

Supported templates:

| Template |
|---|
| default |
| clean |
| compact |
| enterprise |
| dark |

---

# Why Template Configs Matter

Teams often want:

- consistent branding
- standardized reporting
- reusable layouts

---

# Current Include/Exclude Architecture

Configs support:

```yaml
sections:
  include:
```

and:

```yaml
sections:
  exclude:
```

---

# Why Include/Exclude Matters

This enables:

- smaller reports
- faster generation
- focused analysis

---

# Current Config File Examples

---

## YAML Example

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

## TOML Example

```toml
mode = "deep"

[report]
format = "html"
template = "dark"
output_dir = "reports/"

[sections]
include = ["summary", "statistics"]
```

---

## JSON Example

```json
{
  "mode": "deep",
  "report": {
    "format": "html",
    "template": "dark",
    "output_dir": "reports/"
  }
}
```

---

# Current Config System Strengths

The current architecture already supports:

- extensibility
- modularity
- future scaling
- multiple formats
- runtime overrides

---

# Architectural Advantages

---

## Modular Parsing

Each file format has isolated parsing logic.

---

## Shared Runtime Format

All configs normalize into a shared structure.

---

## Decoupled Runtime

Profiling systems remain independent from config parsing.

---

# Why This Architecture Is Strong

This separation enables:

- cleaner testing
- easier maintenance
- future extensibility

---

# Current Weaknesses

Current limitations include:

- no schema validation
- no environment configs
- no global configs
- no inheritance system
- no typed config models

---

# Future Configuration Roadmap

---

# Phase 1 — Validation Layer

Future versions should introduce:

```python
Pydantic config schemas
```

Benefits:

- strict validation
- typed configs
- safer parsing

---

# Phase 2 — Environment Configs

Future support:

```text
aniwa.dev.yaml
aniwa.prod.yaml
aniwa.ci.yaml
```

---

# Why Environment Configs Matter

This enables:

- CI pipelines
- team workflows
- deployment consistency

---

# Phase 3 — Global User Configs

Future support:

```text
~/.aniwa/config.yaml
```

---

# Benefits of Global Configs

Users can define:

- default templates
- preferred outputs
- standard modes

---

# Phase 4 — Config Inheritance

Future support:

```yaml
extends: base.yaml
```

---

# Benefits of Inheritance

This enables:

- enterprise presets
- reusable configurations
- standardized workflows

---

# Phase 5 — Plugin Configurations

Future plugins may register config namespaces.

Example:

```yaml
plugins:
  pii_detector:
    enabled: true
```

---

# Why Plugin Configs Matter

Future extensibility depends heavily on namespaced configs.

---

# Phase 6 — Database Connectivity Configs

Future database systems may support:

```yaml
connections:
  postgres:
```

---

# Future Cloud Configurations

Potential future integrations:

- S3
- Snowflake
- BigQuery
- Azure Blob Storage

---

# Future Secrets Management

Future systems may integrate:

- environment variables
- vault systems
- cloud secret managers

---

# Long-Term Vision

The configuration system is foundational for turning Aniwa into:

```text
a scalable data intelligence platform
```

rather than only:

```text
a local CLI tool
```

---

# Configuration System Design Principles

---

## Keep Configs Human-Readable

Avoid overly complex syntax.

---

## Prioritize Predictability

Configs should behave consistently.

---

## Avoid Hidden Magic

Resolution order should remain explicit.

---

## Support Automation

Configs should integrate naturally into CI/CD workflows.

---

# Common Mistakes to Avoid

---

## Overcomplicated Schemas

Complex config systems hurt usability.

---

## Tight CLI Coupling

Config systems should remain independent.

---

## Hidden Defaults

Defaults should be documented clearly.

---

## Silent Failures

Invalid configs should never fail silently.

---

# Testing Philosophy

Configuration systems require extensive testing.

---

# Current Testing Areas

Tests should validate:

- YAML parsing
- TOML parsing
- JSON parsing
- config discovery
- runtime overrides
- invalid config handling

---

# Future Testing Areas

Future tests should include:

- inheritance
- environment configs
- schema validation
- plugin namespaces

---

# Summary

Aniwa’s configuration system provides:

- reusable workflows
- automation support
- team standardization
- scalable architecture
- CI/CD compatibility
- future extensibility

It is one of the foundational systems that will enable Aniwa to scale from:

```text
a profiling tool
```

into:

```text
a modern data intelligence platform
```

---

# Related Documentation

Continue with:

- architecture/reporting-system.md
- architecture/cli-system.md
- architecture/profiler-system.md
- api/config.md
- user-guide/configuration.md