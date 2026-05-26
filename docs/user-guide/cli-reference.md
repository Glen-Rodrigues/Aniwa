# CLI Reference

This document provides the complete command-line interface reference for Aniwa.

---

# Basic Syntax

```bash
aniwa [OPTIONS] PATH
```

Example:

```bash
aniwa examples/customers.csv
```

---

# Core Command

Aniwa currently exposes a primary profiling command:

```bash
aniwa profile
```

However, the CLI is designed so users can simply run:

```bash
aniwa dataset.csv
```

---

# Required Arguments

---

## PATH

Path to dataset file.

Example:

```bash
aniwa examples/customers.csv
```

Supported file types:

- CSV
- Excel
- JSON
- Parquet

---

# CLI Options

---

## --report

Specify report format.

Short form:

```bash
-r
```

Example:

```bash
aniwa dataset.csv --report html
```

Supported values:

- console
- json
- html
- excel
- markdown
- pdf

---

## --output

Specify explicit output filename.

Short form:

```bash
-o
```

Example:

```bash
aniwa dataset.csv \
  --report html \
  --output profile.html
```

---

## --output-dir

Generate reports into a directory.

Example:

```bash
aniwa dataset.csv \
  --report pdf \
  --output-dir reports/
```

Aniwa automatically:

- creates directories
- generates filenames
- applies extensions

Generated example:

```text
reports/aniwa_report.pdf
```

---

## --mode

Specify profiling mode.

Short form:

```bash
-m
```

Example:

```bash
aniwa dataset.csv --mode fast
```

Supported values:

- fast
- deep

---

## --include

Include specific report sections.

Short form:

```bash
-i
```

Example:

```bash
aniwa dataset.csv \
  --include summary,statistics
```

---

## --exclude

Exclude report sections.

Short form:

```bash
-e
```

Example:

```bash
aniwa dataset.csv \
  --exclude charts
```

---

## --template

Specify report template.

Short form:

```bash
-t
```

Example:

```bash
aniwa dataset.csv \
  --report html \
  --template dark
```

Supported templates:

- default
- clean
- compact
- enterprise
- dark

---

## --config

Specify custom configuration file.

Short form:

```bash
-c
```

Example:

```bash
aniwa dataset.csv \
  --config examples/config_sample.yaml
```

---

# Complete Examples

---

## Console Profiling

```bash
aniwa examples/customers.csv
```

---

## JSON Report

```bash
aniwa examples/customers.csv \
  --report json \
  --output profile.json
```

---

## HTML Report

```bash
aniwa examples/customers.csv \
  --report html \
  --template dark \
  --output profile.html
```

---

## PDF Report

```bash
aniwa examples/customers.csv \
  --report pdf \
  --template enterprise
```

---

## Fast Profiling

```bash
aniwa examples/customers.csv --mode fast
```

---

## Deep Profiling

```bash
aniwa examples/customers.csv --mode deep
```

---

## Include Sections

```bash
aniwa examples/customers.csv \
  --include summary,insights
```

---

## Exclude Sections

```bash
aniwa examples/customers.csv \
  --exclude statistics
```

---

## Output Directory

```bash
aniwa examples/customers.csv \
  --report html \
  --output-dir reports/
```

---

## Custom Config

```bash
aniwa examples/customers.csv \
  --config configs/team.yaml
```

---

# Report Sections

Supported sections:

- summary
- schema
- quality
- statistics
- insights
- charts

---

# Report Templates

---

## default

Balanced modern design.

---

## clean

Minimal lightweight appearance.

---

## compact

Dense information-focused layout.

---

## enterprise

Professional executive-style reporting.

---

## dark

Dark-mode optimized reporting.

---

# Profiling Modes

---

## fast

Optimized for:

- speed
- large datasets
- lightweight inspection

---

## deep

Optimized for:

- completeness
- audits
- intelligent analysis

---

# Configuration Discovery

Aniwa automatically searches for:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

in the current working directory.

---

# CLI Override Rules

Priority order:

```text
CLI arguments > Config file > Defaults
```

---

# Error Examples

---

## Invalid Section

```text
Invalid report section: metrics
```

---

## Invalid Mode

```text
Invalid profiling mode: ultra
```

---

## Missing File

```text
File does not exist: dataset.csv
```

---

## Conflicting Output Arguments

```text
Use either --output or --output-dir, not both.
```

---

# Internal CLI Architecture

Primary CLI logic exists in:

```text
aniwa/cli.py
```

Responsibilities include:

- argument parsing
- validation
- config loading
- execution orchestration
- report routing
- metadata generation

---

# Recommended Usage Patterns

---

## Exploration

```bash
aniwa dataset.csv
```

---

## Reporting

```bash
aniwa dataset.csv --report html
```

---

## Automation

```bash
aniwa dataset.csv --report json
```

---

## Governance

```bash
aniwa dataset.csv \
  --report pdf \
  --template enterprise
```

---

# Future CLI Roadmap

Future planned CLI capabilities:

- plugin commands
- interactive mode
- database connections
- streaming datasets
- remote profiling
- distributed execution
- cloud integrations
- AI-assisted analysis

---

# Best Practices

Recommended practices:

- use config files for teams
- standardize report templates
- automate profiling workflows
- use deep mode for audits
- use fast mode for CI

---

# Next Steps

Continue with:

- profiling-modes.md
- report-formats.md
- report-templates.md
- sections.md