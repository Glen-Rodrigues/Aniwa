# Profiler API

The profiler is the core intelligence engine of Aniwa.

It is responsible for transforming raw datasets into structured profiling intelligence.

The profiler powers:

- schema analysis
- quality analysis
- statistical profiling
- intelligent insights
- metadata generation
- reporting pipelines

Everything in Aniwa ultimately flows through the profiler.

---

# What the Profiler Does

At a high level:

```text
dataset
→ profiler
→ structured intelligence
```

The profiler converts unknown datasets into understandable information.

---

# Core Philosophy

Aniwa's profiler is designed to be:

- modular
- scalable
- extensible
- format-agnostic
- automation-friendly
- intelligence-oriented

---

# Profiler Architecture

Current architecture:

```text
CLI
→ dataset reader
→ dataframe
→ profiler
→ DatasetProfile
→ reports
```

---

# Primary Profiler Entry Point

Main profiling function:

```python
profile_dataframe()
```

This is the central profiling engine.

---

# Current Function Flow

```text
DataFrame
→ profiling pipeline
→ section analysis
→ insights generation
→ DatasetProfile
```

---

# Profiler File Location

```text
aniwa/core/profiler.py
```

---

# Current Profiler Responsibilities

The profiler currently handles:

- dataset summaries
- schema profiling
- null analysis
- duplicate analysis
- uniqueness analysis
- numeric statistics
- insight generation
- section filtering

---

# Input Architecture

The profiler currently operates on:

```python
Polars DataFrame
```

This creates:

- performance advantages
- scalability benefits
- columnar optimizations

---

# Why Polars?

Aniwa uses Polars because it provides:

- high performance
- memory efficiency
- parallel execution
- modern dataframe architecture
- scalability for large datasets

---

# Current Profiling Pipeline

Current conceptual flow:

```text
read dataset
→ validate dataframe
→ generate summary
→ analyze columns
→ compute quality metrics
→ generate insights
→ build profile
```

---

# Section-Based Architecture

Aniwa uses modular profiling sections.

This allows:

- selective profiling
- performance optimization
- flexible reporting
- scalable extensibility

---

# Current Sections

Current profiling sections:

| Section |
|---|
| summary |
| schema |
| quality |
| statistics |
| insights |
| charts |

---

# Section Resolution

Section flow:

```text
CLI include/exclude
→ resolve_sections()
→ profiler execution
```

---

# Why Modular Sections Matter

Modular sections improve:

- scalability
- performance
- maintainability
- customization
- future plugin systems

---

# Dataset Summary Generation

The profiler generates:

```python
rows
columns
```

using dataframe metadata.

---

# Schema Profiling

The profiler analyzes:

- column names
- data types
- inferred structure

---

# Schema Flow

```text
dataframe columns
→ dtype analysis
→ schema metadata
→ ColumnProfile objects
```

---

# Null Analysis

The profiler calculates:

```python
null_count
null_percent
```

for each column.

---

# Why Null Analysis Matters

Null analysis helps detect:

- incomplete datasets
- ingestion issues
- broken pipelines
- sparse data
- governance risks

---

# Duplicate Analysis

The profiler calculates:

```python
duplicate_rows
duplicate_percent
```

---

# Duplicate Detection Purpose

Duplicate analysis identifies:

- ingestion duplication
- broken ETL systems
- merge problems
- integrity issues

---

# Uniqueness Analysis

The profiler computes:

```python
unique_count
```

for columns.

---

# Why Uniqueness Matters

Uniqueness analysis helps identify:

- primary keys
- identifiers
- high-cardinality columns
- suspicious distributions

---

# Numeric Statistics

The profiler computes:

```python
min
max
mean
median
std
```

for numeric columns.

---

# Numeric Profiling Flow

```text
numeric column
→ statistical analysis
→ NumericStatistics model
```

---

# Insight Engine

Aniwa includes an intelligence layer.

The profiler generates:

- warnings
- recommendations
- suspicious pattern detection

---

# Current Insight Types

Current insight systems include:

- duplicate warnings
- sparse column warnings
- possible sensitive data detection
- suspicious quality patterns

---

# Sensitive Data Detection

Aniwa can detect columns that may contain:

- emails
- identifiers
- personal information

based on naming heuristics.

---

# Insight Generation Flow

```text
profiling results
→ rule engine
→ Insight objects
```

---

# Fast vs Deep Profiling

Aniwa currently supports:

```python
ProfileMode.fast
ProfileMode.deep
```

---

# Fast Mode

Fast mode prioritizes:

- speed
- lightweight analysis
- quick inspection

---

# Deep Mode

Deep mode prioritizes:

- richer statistics
- complete profiling
- more intelligence generation

---

# Current Performance Philosophy

Aniwa prioritizes:

- developer experience
- responsiveness
- scalability
- intelligent defaults

---

# Current Scalability Model

The profiler currently scales through:

- Polars optimizations
- vectorized operations
- columnar execution
- efficient dataframe operations

---

# Future Scalability Vision

Future systems may support:

- distributed profiling
- chunked profiling
- streaming datasets
- lazy execution
- cloud-native execution

---

# Chunked Profiling Vision

Future profiling may support:

```text
dataset chunks
→ incremental analysis
→ aggregated results
```

for very large datasets.

---

# Distributed Profiling Vision

Future architecture may distribute profiling across:

- worker nodes
- clusters
- cloud infrastructure

---

# Streaming Profiling Vision

Future streaming systems may analyze:

- Kafka streams
- event pipelines
- real-time ingestion systems

---

# Profiling Extensibility

Aniwa is intentionally designed to support future extensions.

---

# Future Statistical Features

Future profiling may include:

- correlations
- covariance
- skewness
- kurtosis
- quantiles
- histograms

---

# Future AI Features

Future intelligence systems may include:

- semantic understanding
- dataset summarization
- anomaly explanation
- AI recommendations
- natural language insights

---

# Future Governance Features

Future governance systems may include:

- trust scoring
- schema drift detection
- policy validation
- lineage tracking
- compliance analysis

---

# Future Semantic Profiling

Future systems may detect:

- addresses
- phone numbers
- financial fields
- geospatial data
- timestamps
- business entities

---

# Future Relationship Detection

Future systems may infer:

- foreign keys
- relational structures
- entity relationships
- graph dependencies

---

# Internal Profiler Design Philosophy

The profiler should remain:

- modular
- composable
- extensible
- testable
- deterministic

---

# Separation of Concerns

The profiler is intentionally separated from:

- CLI logic
- report rendering
- file IO
- presentation systems

---

# Why Separation Matters

This separation enables:

- easier testing
- cleaner architecture
- future APIs
- cloud deployments
- distributed systems

---

# Report Independence

The profiler produces:

```python
DatasetProfile
```

which can be consumed by:

- HTML reports
- PDF reports
- JSON exports
- console views
- APIs

without changing profiling logic.

---

# Internal Pipeline Stability

Stable profiler outputs create:

- stable reports
- reliable integrations
- predictable APIs
- easier refactoring

---

# Error Handling Philosophy

The profiler prioritizes:

- graceful failures
- meaningful errors
- deterministic behavior
- recoverability

---

# Validation Philosophy

The profiler validates:

- section inputs
- profiling modes
- dataset structures
- report compatibility

---

# Testing Philosophy

Profiler testing focuses on:

- correctness
- reproducibility
- edge cases
- dataset variability

---

# Example Profiler Test Flow

```text
input dataset
→ profile_dataframe()
→ assert profile structure
```

---

# Future Benchmarking

Future systems may benchmark:

- execution time
- memory usage
- scalability
- throughput
- parallel performance

---

# Enterprise Profiling Vision

Future enterprise profiling may support:

- petabyte-scale datasets
- governance enforcement
- centralized profiling systems
- automated quality monitoring
- organizational trust systems

---

# AI-Native Profiling Vision

Future AI systems may enable:

- conversational dataset understanding
- autonomous quality checks
- semantic recommendations
- natural language explanations

---

# Long-Term Architectural Role

The profiler is the heart of Aniwa.

Everything else exists to:

- support it
- present it
- extend it
- operationalize it

---

# Summary

Aniwa's profiler provides:

- schema analysis
- quality analysis
- statistics
- intelligent insights
- modular profiling
- scalable architecture
- future extensibility

It is the central intelligence engine of the platform.

---

# Related Documentation

Continue with:

- architecture/core-engine.md
- architecture/reporting-system.md
- architecture/cli.md
- api/models.md