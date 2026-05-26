# Examples

This guide provides practical Aniwa usage examples for common profiling workflows.

These examples demonstrate:

- dataset inspection
- report generation
- configuration usage
- automation workflows
- profiling strategies

---

# Basic Dataset Profiling

Profile a CSV dataset:

```bash
aniwa examples/customers.csv
```

Profile an Excel dataset:

```bash
aniwa examples/customers.xlsx
```

Profile a JSON dataset:

```bash
aniwa examples/customers.json
```

Profile a Parquet dataset:

```bash
aniwa examples/customers.parquet
```

---

# Fast Profiling

Use lightweight profiling for speed:

```bash
aniwa examples/customers.csv --mode fast
```

Best for:

- quick inspections
- CI validation
- very large datasets

---

# Deep Profiling

Run comprehensive profiling:

```bash
aniwa examples/customers.csv --mode deep
```

Best for:

- audits
- production validation
- deep analysis

---

# JSON Reports

Generate machine-readable reports:

```bash
aniwa examples/customers.csv \
  --report json \
  --output reports/profile.json
```

Use cases:

- automation
- APIs
- pipelines
- integrations

---

# HTML Reports

Generate shareable HTML reports:

```bash
aniwa examples/customers.csv \
  --report html \
  --output reports/profile.html
```

Best for:

- stakeholders
- sharing
- auditing
- visualization

---

# PDF Reports

Generate printable reports:

```bash
aniwa examples/customers.csv \
  --report pdf \
  --output reports/profile.pdf
```

Best for:

- compliance
- documentation
- management reviews

---

# Markdown Reports

Generate GitHub-friendly reports:

```bash
aniwa examples/customers.csv \
  --report markdown \
  --output reports/profile.md
```

Best for:

- documentation
- GitHub issues
- pull requests

---

# Excel Reports

Generate spreadsheet reports:

```bash
aniwa examples/customers.csv \
  --report excel \
  --output reports/profile.xlsx
```

Best for:

- analysts
- spreadsheet workflows
- exports

---

# Using Templates

---

## Dark Template

```bash
aniwa examples/customers.csv \
  --report html \
  --template dark
```

---

## Enterprise Template

```bash
aniwa examples/customers.csv \
  --report pdf \
  --template enterprise
```

---

## Compact Template

```bash
aniwa examples/customers.csv \
  --report html \
  --template compact
```

---

# Output Directories

Generate reports into folders:

```bash
aniwa examples/customers.csv \
  --report html \
  --output-dir reports/
```

Generated output:

```text
reports/aniwa_report.html
```

---

# Include Specific Sections

Generate focused reports:

```bash
aniwa examples/customers.csv \
  --include summary,insights
```

---

# Exclude Sections

Remove unnecessary sections:

```bash
aniwa examples/customers.csv \
  --exclude statistics
```

---

# Configuration File Examples

---

## YAML Workflow

`aniwa.yaml`

```yaml
mode: deep

report:
  format: html
  template: enterprise
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

---

## Custom Config File

```bash
aniwa examples/customers.csv \
  --config examples/config_sample.yaml
```

---

# Automation Examples

---

## Nightly Profiling

```bash
aniwa production/customers.csv \
  --report html \
  --output-dir nightly_reports/
```

---

## CI Validation

```bash
aniwa production/customers.csv \
  --mode fast \
  --report json
```

---

## Audit Workflow

```bash
aniwa production/customers.csv \
  --mode deep \
  --report pdf \
  --template enterprise
```

---

# Example Profiling Insights

Aniwa can generate insights like:

```text
1 duplicate rows detected.
```

```text
Column 'email' may contain sensitive information.
```

```text
Column 'customer_id' may represent an identifier.
```

```text
Column 'revenue' has high cardinality.
```

---

# Example Enterprise Workflow

---

## Step 1 — Initial Inspection

```bash
aniwa customers.csv
```

---

## Step 2 — Generate HTML Report

```bash
aniwa customers.csv \
  --report html
```

---

## Step 3 — Generate PDF Audit

```bash
aniwa customers.csv \
  --report pdf \
  --template enterprise
```

---

## Step 4 — Standardize with Config

`aniwa.yaml`

```yaml
mode: deep

report:
  format: pdf
  template: enterprise
  output_dir: audits/
```

---

## Step 5 — Automate

```bash
aniwa customers.csv
```

---

# Example Team Structure

```text
project/
├── datasets/
├── reports/
├── configs/
├── audits/
├── aniwa.yaml
```

---

# Example Data Engineering Workflow

Aniwa fits naturally into:

```text
ingestion
→ validation
→ profiling
→ quality checks
→ transformation
→ analytics
```

---

# Example Governance Workflow

Aniwa can support:

- dataset audits
- trust reviews
- onboarding datasets
- quality validation
- metadata inspection

---

# Future Workflow Examples

Future versions of Aniwa may support:

- database profiling
- distributed profiling
- observability integration
- AI-assisted insights
- dataset lineage
- semantic understanding
- trust scoring

---

# Recommended Practice

A recommended workflow:

1. inspect datasets immediately
2. generate reusable reports
3. standardize configs
4. automate validation
5. integrate into CI/CD

---

# Next Steps

Continue with:

- cli-reference.md
- profiling-modes.md
- report-formats.md
- architecture/overview.md