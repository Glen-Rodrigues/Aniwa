# Output Management

Aniwa provides a flexible output management system designed for:

- reproducibility
- automation
- scalability
- developer workflows
- CI/CD pipelines
- governance reporting

Output management controls:

- report destinations
- filenames
- directory handling
- output generation behavior

---

# Why Output Management Matters

Dataset profiling often produces many reports.

Without structured output management:

- reports become disorganized
- pipelines become difficult to maintain
- automation becomes fragile
- governance workflows become inconsistent

Aniwa solves this through predictable output behavior.

---

# Core Output Features

Aniwa currently supports:

- automatic filenames
- output directories
- custom output paths
- automatic directory creation
- format-aware extensions
- output validation

---

# Output Architecture

Internal output flow:

```text
CLI
→ resolve_output_path()
→ ensure_output_parent()
→ renderer
→ final artifact
```

---

# Default Output Behavior

When no output path is provided, Aniwa generates default filenames automatically.

Examples:

| Format | Default Filename |
|---|---|
| html | aniwa_report.html |
| json | aniwa_report.json |
| markdown | aniwa_report.md |
| excel | aniwa_report.xlsx |
| pdf | aniwa_report.pdf |

---

# Console Output Exception

Console reports do not generate files.

Example:

```bash
aniwa dataset.csv
```

Output is rendered directly in the terminal.

---

# Custom Output Paths

Users can explicitly specify output paths.

Example:

```bash
aniwa dataset.csv \
  --report html \
  --output reports/profile.html
```

---

# Output Directory Support

Aniwa supports directory-based report generation.

Example:

```bash
aniwa dataset.csv \
  --report pdf \
  --output-dir reports/
```

Generated output:

```text
reports/aniwa_report.pdf
```

---

# Why Output Directories Matter

Output directories simplify:

- automation
- CI/CD
- batch processing
- report organization

---

# Automatic Directory Creation

Aniwa automatically creates missing directories.

Example:

```bash
aniwa dataset.csv \
  --report html \
  --output-dir reports/daily/
```

Aniwa creates:

```text
reports/
reports/daily/
```

if they do not already exist.

---

# Internal Directory Creation

Internal implementation:

```python
output_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)
```

Benefits:

- automation safety
- reduced setup friction
- pipeline compatibility

---

# Output Validation

Aniwa validates output configuration before report generation.

Examples:

- conflicting output options
- invalid formats
- unsupported templates

---

# Mutually Exclusive Options

The following options cannot be used together:

- `--output`
- `--output-dir`

Incorrect:

```bash
aniwa dataset.csv \
  --output report.html \
  --output-dir reports/
```

Result:

```text
Use either --output or --output-dir, not both.
```

---

# Why Mutual Exclusivity Exists

Allowing both options introduces ambiguity.

Questions include:

- which path takes precedence?
- should filenames be overridden?
- should directories wrap explicit filenames?

Aniwa avoids this complexity through explicit validation.

---

# Output Filename Resolution

Internal filename resolution:

```python
resolve_default_name(report)
```

Example mapping:

```python
{
    ReportFormat.html: "aniwa_report.html"
}
```

---

# Output Extension Resolution

Extensions are automatically matched to report formats.

Examples:

| Format | Extension |
|---|---|
| html | .html |
| json | .json |
| markdown | .md |
| excel | .xlsx |
| pdf | .pdf |

---

# Output Path Resolution Flow

Internal flow:

```text
output specified?
→ yes → use explicit path

output_dir specified?
→ yes → generate filename in directory

otherwise
→ generate default filename
```

---

# Output and Configuration Files

Output settings may be defined in config files.

Example:

```yaml
report:
  output_dir: reports/
```

---

# CLI Override Priority

Priority order:

```text
CLI > config > defaults
```

---

# Example Override

Config:

```yaml
report:
  output_dir: reports/
```

CLI:

```bash
aniwa dataset.csv \
  --output final/report.html
```

Final output:

```text
final/report.html
```

---

# Batch Profiling Workflows

Output management is critical for batch workflows.

Example:

```bash
aniwa customers.csv --output-dir reports/
aniwa orders.csv --output-dir reports/
aniwa payments.csv --output-dir reports/
```

---

# CI/CD Workflow Benefits

Output directories improve CI pipelines.

Example:

```bash
aniwa dataset.csv \
  --report json \
  --output-dir artifacts/
```

Benefits:

- organized artifacts
- reproducible outputs
- easier uploads

---

# Governance Workflow Benefits

Governance workflows often require archival reports.

Example:

```bash
aniwa dataset.csv \
  --report pdf \
  --output-dir audits/
```

---

# Recommended Output Structures

---

## Small Projects

```text
reports/
```

---

## Medium Projects

```text
reports/
├── html/
├── pdf/
└── json/
```

---

## Enterprise Projects

```text
artifacts/
├── daily/
├── governance/
├── audits/
├── monitoring/
└── snapshots/
```

---

# Future Output Management Goals

Future improvements may include:

- timestamped filenames
- dataset-based filenames
- versioned outputs
- incremental reports
- output compression
- remote storage

---

# Timestamped Outputs

Possible future behavior:

```text
aniwa_report_2026_05_26.html
```

Benefits:

- historical tracking
- report archival
- governance traceability

---

# Dataset-Aware Filenames

Possible future behavior:

```text
customers_profile.html
orders_profile.html
```

---

# Incremental Profiling Outputs

Future systems may support:

```text
daily snapshots
→ profile history
→ change tracking
```

---

# Cloud Output Vision

Future integrations may support:

- S3
- GCS
- Azure Blob
- remote storage systems

---

# Remote Artifact Vision

Possible future architecture:

```text
Aniwa
→ local output
→ cloud artifact storage
→ governance systems
```

---

# Enterprise Output Policies

Future enterprise systems may enforce:

- naming conventions
- retention policies
- governance standards
- archival requirements

---

# Output Security Considerations

Reports may contain:

- metadata
- schema information
- sensitive insights

Future systems may support:

- encrypted reports
- secure output locations
- access control

---

# Observability Integration Vision

Future systems may expose outputs to:

- observability platforms
- monitoring systems
- governance dashboards

---

# Plugin Output Systems

Future plugins may define custom output types.

Example:

```text
plugins/
→ custom report exporters
→ governance bundles
→ ML validation outputs
```

---

# Best Practices

---

## Organize Outputs Early

Avoid cluttered project roots.

---

## Use Separate Artifact Folders

Examples:

- reports/
- artifacts/
- audits/

---

## Keep Reports Versioned

Useful for governance and debugging.

---

## Use Output Directories in CI/CD

Improves automation consistency.

---

# Common Mistakes

---

## Mixing Output Options

Incorrect:

```bash
--output report.html --output-dir reports/
```

---

## Forgetting File Extensions

Explicit output paths should include proper extensions.

Correct:

```bash
--output report.html
```

---

## Overwriting Important Reports

Default filenames may overwrite previous outputs.

Future timestamp support may address this.

---

# Long-Term Vision

Output management is foundational to Aniwa becoming:

- a profiling platform
- a governance system
- an observability engine
- a scalable data intelligence ecosystem

---

# Summary

Aniwa output management provides:

- predictable artifact generation
- scalable report organization
- automation-friendly workflows
- governance compatibility
- future extensibility

It enables Aniwa to scale cleanly from local development to enterprise infrastructure.

---

# Next Steps

Continue with:

- architecture-overview.md
- scalability-roadmap.md
- contributor-guide.md
- testing-guide.md