# Metadata

Aniwa generates profiling metadata alongside every dataset profile.

Metadata provides contextual information about:

- the profiling environment
- dataset source
- runtime details
- report generation settings
- reproducibility information

Metadata is critical for:

- governance
- debugging
- audits
- reproducibility
- CI/CD workflows
- observability

---

# Why Metadata Matters

Without metadata, reports lose context.

Users need to know:

- when a report was generated
- which version created it
- which dataset was profiled
- what profiling settings were used
- how long profiling took

Metadata transforms reports into reproducible profiling artifacts.

---

# Metadata Architecture

Metadata is represented internally using the `ProfileMetadata` model.

Location:

```text
aniwa/models/profile.py
```

---

# Metadata Generation Flow

Internal flow:

```text
CLI
→ build_profile_metadata()
→ DatasetProfile.metadata
→ report rendering
```

---

# Metadata Collection

Aniwa collects metadata automatically during profiling.

This requires no additional user configuration.

---

# Current Metadata Fields

Aniwa currently tracks:

| Field | Description |
|---|---|
| generated_at | profiling timestamp |
| aniwa_version | installed Aniwa version |
| python_version | Python runtime version |
| operating_system | host operating system |
| polars_version | installed Polars version |
| dataset_path | source dataset path |
| dataset_file_type | detected dataset format |
| dataset_size | dataset file size |
| profiling_mode | fast or deep |
| report_format | selected report type |
| report_template | active template |
| included_sections | enabled report sections |
| excluded_sections | excluded report sections |
| profiling_duration | execution duration |
| command_used | reconstructed CLI command |

---

# Generated Timestamp

Example:

```text
2026-05-26 07:12:53 UTC
```

Purpose:

- reproducibility
- auditing
- historical tracking
- governance logging

---

# Aniwa Version

Example:

```text
0.1.1
```

Purpose:

- debugging
- compatibility tracking
- migration analysis

---

# Python Version

Example:

```text
3.14.4
```

Purpose:

- runtime debugging
- dependency compatibility
- environment diagnostics

---

# Operating System

Example:

```text
Windows 11
```

Purpose:

- platform diagnostics
- issue reproduction
- compatibility validation

---

# Polars Version

Example:

```text
1.40.1
```

Purpose:

- dataframe compatibility
- backend diagnostics
- profiling reproducibility

---

# Dataset Path

Example:

```text
examples/customers.csv
```

Purpose:

- source traceability
- debugging
- workflow reproducibility

---

# Dataset File Type

Example:

```text
CSV
```

Purpose:

- parser tracking
- ingestion validation
- workflow diagnostics

---

# Dataset Size

Example:

```text
197 B
```

Purpose:

- performance analysis
- runtime interpretation
- scaling diagnostics

---

# Profiling Mode

Possible values:

- fast
- deep

Purpose:

- explain profiling depth
- interpret report completeness
- understand runtime tradeoffs

---

# Report Format

Possible values:

- console
- json
- html
- markdown
- excel
- pdf

Purpose:

- rendering diagnostics
- artifact identification

---

# Report Template

Examples:

- default
- clean
- compact
- enterprise
- dark

Purpose:

- styling reproducibility
- branding consistency

---

# Included Sections

Example:

```text
summary, schema, statistics
```

Purpose:

- report interpretation
- modular profiling diagnostics

---

# Excluded Sections

Example:

```text
charts
```

Purpose:

- explain missing report sections
- optimize debugging

---

# Profiling Duration

Example:

```text
0.07s
```

Purpose:

- performance benchmarking
- scaling diagnostics
- optimization analysis

---

# Command Used

Aniwa reconstructs the profiling command automatically.

Example:

```text
aniwa dataset.csv --report html --template dark
```

Purpose:

- reproducibility
- auditing
- workflow recreation

---

# Metadata Rendering

Metadata appears in:

- console reports
- HTML reports
- PDF reports
- JSON reports
- markdown reports

---

# Metadata in Console Reports

Console reports display metadata using Rich tables.

Benefits:

- readability
- structured formatting
- developer-friendly diagnostics

---

# Metadata in HTML Reports

HTML reports render metadata using structured tables.

Benefits:

- visual clarity
- governance presentation
- exportability

---

# Metadata in JSON Reports

JSON reports serialize metadata directly.

Example:

```json
{
  "metadata": {
    "aniwa_version": "0.1.1"
  }
}
```

Benefits:

- machine readability
- automation support
- API integrations

---

# Metadata in Markdown Reports

Markdown reports render metadata as tables.

Benefits:

- GitHub compatibility
- documentation workflows
- issue tracking

---

# Metadata Validation

Metadata is generated internally and validated through typed models.

Benefits:

- consistency
- type safety
- serialization reliability

---

# Internal Metadata Builder

Primary metadata builder:

```python
build_profile_metadata()
```

Responsibilities:

- collect runtime information
- normalize metadata
- format outputs
- attach profile context

---

# Metadata Design Philosophy

Aniwa metadata is designed to be:

- reproducible
- structured
- human-readable
- machine-readable
- extensible

---

# Governance Importance

Metadata is critical for governance workflows.

It supports:

- auditability
- traceability
- compliance
- validation

---

# CI/CD Use Cases

Metadata enables CI/CD systems to track:

- profiling duration
- profiling configuration
- environment details
- report provenance

---

# Observability Vision

Long-term metadata goals include:

- profiling telemetry
- execution metrics
- lineage tracking
- profiling history
- observability integrations

---

# Future Metadata Fields

Planned future metadata may include:

- git commit hashes
- environment names
- cloud provider info
- pipeline IDs
- lineage references
- validation results
- profiling snapshots

---

# Future Profiling Provenance

Future provenance systems may track:

```text
dataset
→ transformations
→ profiling runs
→ validations
→ downstream systems
```

---

# Metadata and Scalability

Metadata becomes increasingly important at scale.

Large organizations require:

- reproducibility
- historical tracking
- governance visibility
- debugging traceability

---

# Enterprise Metadata Vision

Future enterprise metadata may include:

- ownership
- business domains
- governance tags
- sensitivity classifications
- data contracts

---

# Security Considerations

Metadata may expose:

- file paths
- environment details
- runtime systems

Future versions may support:

- metadata redaction
- secure exports
- environment masking

---

# Future Compliance Integrations

Potential future integrations:

- SOC2
- HIPAA
- GDPR
- ISO compliance
- governance auditing

---

# Metadata Performance

Metadata generation is lightweight.

Current overhead is minimal compared to:

- dataframe loading
- statistical analysis
- chart rendering

---

# Best Practices

---

## Preserve Metadata

Do not strip metadata from reports unnecessarily.

---

## Track Versions

Always record profiling tool versions.

---

## Keep Reports Reproducible

Metadata enables future debugging and auditing.

---

# Common Mistakes

---

## Ignoring Profiling Mode

Fast and deep modes produce different profiling depth.

Metadata helps explain this.

---

## Removing Command Context

The `command_used` field is extremely valuable for reproducibility.

---

# Long-Term Vision

Metadata is foundational to Aniwa's evolution into:

- a profiling platform
- a governance platform
- an observability system
- a data intelligence ecosystem

---

# Summary

Aniwa metadata provides:

- reproducibility
- observability
- governance support
- runtime diagnostics
- profiling traceability

It transforms reports from simple outputs into durable profiling artifacts.

---

# Next Steps

Continue with:

- configuration.md
- profiling-modes.md
- output-formats.md
- architecture-overview.md