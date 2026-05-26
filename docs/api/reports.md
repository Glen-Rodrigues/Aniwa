# Reports API

The Reports API is responsible for transforming dataset profiling results into human-readable and machine-readable outputs.

It is one of the most important systems inside Aniwa because it converts raw profiling intelligence into actionable information.

---

# Purpose of the Reports System

The reporting layer exists to:

- visualize profiling results
- communicate dataset intelligence
- support debugging workflows
- enable audits
- improve collaboration
- generate shareable outputs
- support automation systems

---

# High-Level Architecture

```text
dataset
→ profiler
→ DatasetProfile
→ report renderer
→ output file
```

---

# Current Report System Location

```text
aniwa/reports/
```

---

# Current Report Modules

```text
aniwa/reports/
├── console.py
├── json_report.py
├── html_report.py
├── markdown_report.py
├── excel_report.py
└── pdf_report.py
```

---

# Core Reporting Philosophy

Aniwa reports are designed to be:

- readable
- structured
- scalable
- automation-friendly
- developer-friendly
- shareable
- visually clear

---

# Why Reporting Matters

Profiling alone is insufficient.

Users need:

- visibility
- interpretation
- presentation
- exportability

Reports bridge the gap between profiling and decision-making.

---

# Standard Reporting Input

All report renderers receive:

```python
DatasetProfile
```

This creates architectural consistency across all report systems.

---

# Why Standardized Inputs Matter

This design enables:

- modular renderers
- reusable profiling systems
- future extensibility
- cleaner architecture

---

# Current Supported Reports

Aniwa currently supports:

| Report Type | Purpose |
|---|---|
| Console | Interactive terminal output |
| JSON | Machine-readable export |
| HTML | Shareable visual reports |
| Markdown | Documentation-friendly reports |
| Excel | Spreadsheet analysis |
| PDF | Portable reporting |

---

# Report Rendering Flow

```text
DataFrame
→ profiler
→ DatasetProfile
→ renderer
→ output
```

---

# Console Reports

Location:

```text
aniwa/reports/console.py
```

---

# Purpose of Console Reports

Console reports provide:

- instant feedback
- terminal-native UX
- interactive readability
- developer-friendly inspection

---

# Console Rendering Stack

Aniwa uses:

```text
Rich
```

for terminal rendering.

---

# Console Features

Current console reports include:

- dataset summaries
- column profiling
- statistics
- insights
- metadata
- structured tables

---

# Why Rich Matters

Rich enables:

- modern CLI experiences
- readable formatting
- structured layouts
- beautiful terminal UX

---

# Console Design Philosophy

Console output should be:

- readable
- fast
- informative
- visually clean
- low-noise

---

# JSON Reports

Location:

```text
aniwa/reports/json_report.py
```

---

# Purpose of JSON Reports

JSON reports are designed for:

- automation
- APIs
- pipelines
- machine consumption
- integrations

---

# JSON Architecture

```text
DatasetProfile
→ serialization
→ JSON output
```

---

# JSON Benefits

JSON provides:

- interoperability
- portability
- structured exports
- pipeline compatibility

---

# Future JSON Vision

Future JSON systems may support:

- schemas
- versioning
- validation
- enterprise metadata
- lineage exports

---

# HTML Reports

Location:

```text
aniwa/reports/html_report.py
```

---

# Purpose of HTML Reports

HTML reports provide:

- shareable reports
- visual analysis
- stakeholder communication
- browser-based inspection

---

# HTML Architecture

```text
DatasetProfile
→ template engine
→ rendered HTML
```

---

# HTML Templates

Aniwa supports multiple templates:

| Template |
|---|
| default |
| clean |
| compact |
| enterprise |
| dark |

---

# Template Philosophy

Templates allow users to choose reporting styles based on:

- readability
- density
- presentation goals
- organizational branding

---

# HTML Features

HTML reports currently support:

- charts
- metadata
- statistics
- insights
- responsive layouts
- structured sections

---

# Chart System

Charts currently include:

- null percentages
- cardinality
- duplicate analysis

---

# Charting Stack

Aniwa currently uses:

```text
Chart.js
```

---

# Why Chart.js

Chart.js provides:

- lightweight rendering
- browser compatibility
- responsive charts
- easy integration

---

# Future HTML Vision

Future HTML systems may support:

- interactivity
- filtering
- drill-down analysis
- embedded lineage
- live dashboards

---

# Markdown Reports

Location:

```text
aniwa/reports/markdown_report.py
```

---

# Purpose of Markdown Reports

Markdown reports are optimized for:

- GitHub
- documentation
- issue tracking
- audits
- lightweight sharing

---

# Markdown Benefits

Markdown enables:

- portability
- version control
- readability
- documentation integration

---

# Example Use Cases

Markdown reports work well for:

- pull requests
- dataset audits
- governance workflows
- incident analysis

---

# Excel Reports

Location:

```text
aniwa/reports/excel_report.py
```

---

# Purpose of Excel Reports

Excel reports support:

- analysts
- business workflows
- spreadsheet ecosystems
- enterprise compatibility

---

# Excel Architecture

```text
DatasetProfile
→ workbook generation
→ formatted sheets
```

---

# Current Excel Features

Current Excel exports include:

- summary sheets
- schema sheets
- quality analysis
- statistics

---

# Why Excel Still Matters

Excel remains one of the most dominant business tools globally.

Supporting Excel significantly increases adoption potential.

---

# Future Excel Vision

Future systems may include:

- charts
- pivot summaries
- conditional formatting
- governance sheets
- lineage tabs

---

# PDF Reports

Location:

```text
aniwa/reports/pdf_report.py
```

---

# Purpose of PDF Reports

PDF reports support:

- executive summaries
- archival workflows
- enterprise distribution
- offline sharing

---

# PDF Benefits

PDF provides:

- portability
- consistency
- presentation stability
- enterprise compatibility

---

# Future PDF Vision

Future PDF systems may support:

- branded exports
- executive layouts
- advanced visualizations
- enterprise themes

---

# Report Metadata

Aniwa reports include metadata such as:

- generated time
- profiling duration
- report format
- dataset size
- operating system
- Aniwa version

---

# Why Metadata Matters

Metadata enables:

- reproducibility
- auditing
- debugging
- governance
- traceability

---

# Section-Based Reporting

Aniwa supports selective report generation.

Users can include/exclude sections such as:

- summary
- schema
- quality
- statistics
- insights
- charts

---

# Why Selective Sections Matter

This enables:

- smaller reports
- focused workflows
- performance optimization
- custom reporting

---

# Reporting Configuration

Reports can be configured using:

- CLI arguments
- config files
- templates

---

# Configurable Outputs

Current configurable features include:

- report format
- template
- output path
- output directory
- included sections

---

# Output Management

Aniwa supports:

```bash
--output
```

and:

```bash
--output-dir
```

---

# Output Directory System

Aniwa automatically:

- creates directories
- generates filenames
- applies extensions

---

# Reporting Scalability Vision

Future report systems may support:

- distributed rendering
- cloud exports
- streaming reports
- report caching

---

# Enterprise Reporting Vision

Future enterprise features may include:

- governance dashboards
- lineage visualizations
- compliance exports
- observability systems

---

# API Reporting Vision

Future systems may expose reports through:

- REST APIs
- GraphQL
- SDKs
- cloud services

---

# Multi-Format Architecture

Aniwa's reporting architecture is intentionally modular.

This allows:

```text
same profile
→ multiple outputs
```

without duplicating profiling logic.

---

# Why Modular Reporting Matters

Benefits include:

- extensibility
- maintainability
- cleaner architecture
- reusable logic

---

# Report Renderer Philosophy

Renderers should:

- consume profiles
- not profile datasets
- remain format-focused
- avoid business logic

---

# Separation of Concerns

Profiling and reporting are intentionally separated.

This is extremely important architecturally.

---

# Why Separation Matters

Without separation:

- systems become tightly coupled
- testing becomes harder
- extensibility suffers

---

# Report Testing Philosophy

Each report renderer should be independently testable.

---

# Current Testing Areas

Tests validate:

- output generation
- formatting correctness
- template rendering
- export integrity
- chart generation

---

# HTML Template Testing

HTML tests validate:

- template loading
- chart rendering
- conditional sections
- responsive layouts

---

# PDF Testing

PDF tests validate:

- successful rendering
- template compatibility
- chart embedding

---

# Excel Testing

Excel tests validate:

- workbook creation
- worksheet structure
- export consistency

---

# Long-Term Reporting Vision

Aniwa aims to become:

```text
a universal dataset intelligence reporting platform
```

not merely a profiler.

---

# Future Dashboard Vision

Future systems may support:

- live dashboards
- historical profiling
- trend monitoring
- observability platforms

---

# Future Monitoring Vision

Future reporting may integrate with:

- Airflow
- Dagster
- Prefect
- dbt
- CI/CD systems

---

# Governance Reporting Vision

Future governance systems may include:

- trust scores
- policy validation
- compliance reporting
- lineage graphs

---

# AI Reporting Vision

Future AI-enhanced reports may provide:

- dataset summaries
- anomaly explanations
- semantic analysis
- automated recommendations

---

# Best Practices

---

## Keep Renderers Isolated

Renderers should only transform profiles into outputs.

---

## Avoid Business Logic

Profiling logic belongs in the profiler system.

---

## Standardize Inputs

All renderers should consume:

```python
DatasetProfile
```

---

## Prioritize Readability

Reports should optimize clarity over visual complexity.

---

# Common Mistakes

---

## Mixing Profiling Into Reports

Bad architecture:

```python
render_and_profile()
```

---

## Tight Coupling

Avoid hardcoding report assumptions.

---

## Duplicating Logic

Shared transformations should remain centralized.

---

# Summary

Aniwa's Reports API provides:

- console rendering
- structured exports
- HTML visualization
- spreadsheet generation
- PDF generation
- automation-friendly outputs
- scalable reporting architecture

The reporting layer transforms profiling intelligence into usable information.

---

# Related Documentation

Continue with:

- api/models.md
- api/profiler.md
- architecture/reporting-system.md
- user-guide/reporting.md
- user-guide/templates.md