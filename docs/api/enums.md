# Enums API

Aniwa uses enums to create:

- predictable APIs
- safer internal logic
- consistent validation
- scalable architecture
- maintainable CLI systems

Enums are foundational to Aniwa's internal architecture.

---

# Why Enums Matter

Without enums:

- string values become fragile
- validation becomes repetitive
- typos become dangerous
- architecture becomes inconsistent

Enums solve this by creating controlled value systems.

---

# Current Enum Architecture

Aniwa currently uses enums for:

- report formats
- profiling modes
- report sections

Future versions may expand enums across:

- connectors
- plugins
- AI systems
- governance engines
- profiling engines

---

# Enum Design Philosophy

Aniwa enums are designed to be:

- explicit
- readable
- scalable
- developer-friendly
- CLI-compatible

---

# Current Enum Files

```text
aniwa/models/enums.py
aniwa/cli.py
```

---

# Core Enum Systems

---

# ReportFormat Enum

Defines all supported report outputs.

Current implementation:

```python
class ReportFormat(str, Enum):
    console = "console"
    json = "json"
    html = "html"
    excel = "excel"
    markdown = "markdown"
    pdf = "pdf"
```

---

# Purpose of ReportFormat

Controls:

- CLI validation
- report routing
- output generation
- default filenames
- renderer selection

---

# ReportFormat Flow

```text
CLI argument
→ ReportFormat enum
→ renderer selection
→ output generation
```

---

# ReportFormat Usage

Example:

```bash
aniwa customers.csv --report html
```

Internal resolution:

```python
ReportFormat.html
```

---

# Renderer Mapping

Current renderer relationships:

| Enum | Renderer |
|---|---|
| console | render_console_report |
| json | render_json_report |
| html | render_html_report |
| excel | render_excel_report |
| markdown | render_markdown_report |
| pdf | render_pdf_report |

---

# Default Filename Resolution

Enums help resolve default output names.

Example:

```python
resolve_default_name(ReportFormat.html)
```

Result:

```text
aniwa_report.html
```

---

# ProfileMode Enum

Defines profiling depth behavior.

Current implementation:

```python
class ProfileMode(str, Enum):
    fast = "fast"
    deep = "deep"
```

---

# Purpose of ProfileMode

Controls:

- profiling depth
- performance behavior
- analysis intensity
- future optimization systems

---

# Fast Mode

Fast mode prioritizes:

- speed
- lightweight analysis
- rapid inspection

Designed for:

- large datasets
- quick debugging
- exploratory workflows

---

# Deep Mode

Deep mode prioritizes:

- completeness
- richer analysis
- full intelligence workflows

Designed for:

- audits
- governance
- reporting
- production validation

---

# ProfileMode Flow

```text
CLI mode
→ ProfileMode enum
→ profiler engine behavior
```

---

# Current Usage

Example:

```bash
aniwa customers.csv --mode deep
```

Internal resolution:

```python
ProfileMode.deep
```

---

# ReportSection Enum

Defines modular profiling sections.

Current implementation concept:

```python
class ReportSection(str, Enum):
    summary = "summary"
    schema = "schema"
    quality = "quality"
    statistics = "statistics"
    insights = "insights"
    charts = "charts"
```

---

# Purpose of ReportSection

Controls:

- modular profiling
- selective reporting
- performance optimization
- output customization

---

# ReportSection Flow

```text
CLI include/exclude
→ ReportSection enum
→ section filtering
→ report generation
```

---

# Include System

Example:

```bash
aniwa customers.csv --include summary,statistics
```

Internal resolution:

```python
{
    ReportSection.summary,
    ReportSection.statistics
}
```

---

# Exclude System

Example:

```bash
aniwa customers.csv --exclude charts
```

Internal resolution:

```python
all_sections - {ReportSection.charts}
```

---

# Validation Benefits

Enums automatically prevent invalid values.

Example:

```bash
aniwa customers.csv --mode ultra
```

Produces:

```text
Invalid profiling mode: ultra
```

---

# CLI Safety Benefits

Enums provide:

- autocomplete-friendly systems
- strict validation
- safer routing
- reduced runtime errors

---

# Enum Resolution Helpers

Aniwa includes helper systems:

```python
resolve_report_format()
resolve_profile_mode()
```

These normalize:

- raw strings
- config values
- CLI values

into validated enums.

---

# Internal Validation Architecture

Flow:

```text
raw value
→ enum resolution
→ validation
→ internal usage
```

---

# Why String Enums?

Aniwa enums inherit from:

```python
str
```

and:

```python
Enum
```

Example:

```python
class ReportFormat(str, Enum):
```

Benefits:

- JSON compatibility
- CLI compatibility
- easier serialization
- cleaner logs
- better developer ergonomics

---

# Enum Serialization

Enums serialize cleanly.

Example:

```python
ReportFormat.html.value
```

Result:

```text
html
```

---

# Enum Scalability

Enums are designed for future expansion.

---

# Future Report Formats

Possible future formats:

```python
csv
xml
yaml
parquet
feather
arrow
```

---

# Future Profiling Modes

Possible future modes:

```python
streaming
distributed
ai
governance
realtime
```

---

# Future Sections

Possible future sections:

```python
correlations
outliers
lineage
semantic_analysis
anomaly_detection
trust_scores
```

---

# Future Connector Enums

Future systems may define:

```python
DatabaseConnector
CloudProvider
StorageEngine
```

---

# Future AI Enums

Future AI systems may define:

```python
InsightSeverity
RecommendationType
SemanticCategory
```

---

# Architectural Importance

Enums create:

- stable APIs
- predictable systems
- scalable architecture
- maintainable workflows

They are foundational infrastructure.

---

# Best Practices

---

## Always Validate External Values

Never trust raw CLI or config values.

Always resolve through enums.

---

## Use Enums Internally

Avoid raw strings in core systems.

Prefer:

```python
ReportFormat.html
```

instead of:

```python
"html"
```

---

## Centralize Enum Definitions

Avoid duplicate enum systems.

Keep enums centralized.

---

## Keep Enums Explicit

Avoid ambiguous values.

Bad:

```python
class Mode:
    a = "a"
```

Good:

```python
class ProfileMode:
    deep = "deep"
```

---

# Common Mistakes

---

## Using Raw Strings Everywhere

Bad:

```python
if report == "html":
```

Better:

```python
if report == ReportFormat.html:
```

---

## Mixing Enums and Strings

Maintain consistency across systems.

---

## Duplicating Enum Logic

Centralize enum validation.

---

# Long-Term Vision

Enums will eventually power:

- plugins
- distributed systems
- AI orchestration
- governance engines
- enterprise workflows
- cloud connectors
- semantic profiling

---

# Enterprise Architecture Vision

Future enterprise systems may use enums for:

- compliance policies
- governance standards
- profiling profiles
- organization-wide configurations

---

# Summary

Aniwa enums provide:

- validation
- routing
- consistency
- scalability
- safer architecture
- maintainable APIs

Enums are a critical architectural foundation of Aniwa.

---

# Related Documentation

Continue with:

- api/reporting.md
- api/profiler.md
- architecture/core-engine.md
- architecture/cli.md