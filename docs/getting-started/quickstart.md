# Quick Start

This guide helps you begin profiling datasets with Aniwa in minutes.

---

# Your First Profile

Run your first dataset profile:

```bash
aniwa customers.csv
```

Aniwa automatically:

- loads the dataset
- infers schema information
- detects quality issues
- calculates statistics
- generates intelligent insights
- renders a Rich terminal report

---

# Example Dataset

Example datasets are available inside:

```text
examples/
```

Example:

```bash
aniwa examples/customers.csv
```

---

# Console Output

Example output:

```text
╭──────────────────────────────╮
│ Aniwa                        │
│ Universal dataset profiling  │
╰──────────────────────────────╯

Dataset Summary
Rows: 5
Columns: 5

Column Profile
customer_id | Int64
email       | String

Insights
- duplicate rows detected
- possible sensitive information detected
```

---

# Generate Reports

Aniwa supports multiple report formats.

---

## JSON Report

```bash
aniwa examples/customers.csv --report json --output profile.json
```

---

## HTML Report

```bash
aniwa examples/customers.csv --report html --output profile.html
```

---

## Markdown Report

```bash
aniwa examples/customers.csv --report markdown --output profile.md
```

---

## Excel Report

```bash
aniwa examples/customers.csv --report excel --output profile.xlsx
```

---

## PDF Report

```bash
aniwa examples/customers.csv --report pdf --output profile.pdf
```

---

# Profiling Modes

Aniwa supports two profiling modes.

---

## Fast Mode

Optimized for speed.

```bash
aniwa examples/customers.csv --mode fast
```

Fast mode focuses on:

- lightweight checks
- rapid schema inspection
- minimal computation

Best for:

- very large datasets
- quick debugging
- CI pipelines

---

## Deep Mode

Comprehensive profiling.

```bash
aniwa examples/customers.csv --mode deep
```

Deep mode includes:

- full statistics
- quality analysis
- deeper insights
- intelligent detection

Best for:

- audits
- production validation
- dataset exploration

---

# Using Report Templates

Aniwa supports multiple report templates.

Available templates:

- default
- clean
- compact
- enterprise
- dark

Example:

```bash
aniwa examples/customers.csv \
  --report html \
  --template dark
```

---

# Output Directories

Automatically generate reports into directories.

```bash
aniwa examples/customers.csv \
  --report html \
  --output-dir reports/
```

Aniwa automatically:

- creates directories
- generates filenames
- applies correct extensions

Generated file example:

```text
reports/aniwa_report.html
```

---

# Include Specific Sections

Generate focused reports.

Example:

```bash
aniwa examples/customers.csv \
  --include summary,insights
```

---

# Exclude Sections

Example:

```bash
aniwa examples/customers.csv \
  --exclude statistics
```

---

# Supported Sections

Available report sections:

- summary
- schema
- quality
- statistics
- insights
- charts

---

# Configuration Files

Aniwa supports reusable project configurations.

Supported config files:

- aniwa.yaml
- aniwa.yml
- aniwa.toml
- aniwa.json

Example:

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

Run:

```bash
aniwa examples/customers.csv
```

Aniwa automatically discovers and loads the config.

---

# Custom Config File

Use a specific config file:

```bash
aniwa examples/customers.csv \
  --config examples/config_sample.yaml
```

---

# CLI Overrides Config

CLI arguments always override config values.

Example:

```bash
aniwa examples/customers.csv \
  --mode fast
```

Overrides:

```yaml
mode: deep
```

---

# Common Workflows

---

## Quick Inspection

```bash
aniwa dataset.csv
```

---

## Team Report Generation

```bash
aniwa dataset.csv \
  --report html \
  --template enterprise \
  --output-dir reports/
```

---

## CI Validation

```bash
aniwa dataset.csv \
  --mode fast \
  --report json
```

---

## Data Audit

```bash
aniwa dataset.csv \
  --mode deep \
  --report pdf
```

---

# Recommended Workflow

A recommended professional workflow:

1. run quick console profile
2. inspect insights
3. generate HTML/PDF reports
4. configure reusable workflows
5. automate in CI/CD pipelines

---

# Next Steps

Continue with:

- first-profile.md
- configuration.md
- cli-reference.md
- profiling-modes.md
- report-formats.md