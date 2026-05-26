# Models API

Aniwa uses structured data models to create:

- predictable architecture
- maintainable systems
- type-safe workflows
- scalable profiling pipelines
- reliable reporting systems

Models are one of the most important architectural layers in Aniwa.

---

# Why Models Matter

Without structured models:

- systems become inconsistent
- outputs become fragile
- validation becomes difficult
- reporting becomes unreliable
- scalability becomes painful

Models solve these problems by defining strict internal structures.

---

# Model Architecture Philosophy

Aniwa models are designed around:

- clarity
- composability
- immutability-friendly workflows
- scalability
- serialization compatibility
- report portability

---

# Current Model Responsibilities

Aniwa models currently manage:

- dataset summaries
- schema profiling
- numeric statistics
- quality analysis
- profiling insights
- metadata
- report structures

---

# Model Layer Architecture

```text
dataset
→ profiler
→ models
→ reports
→ outputs
```

---

# Core Model Location

Current structure:

```text
aniwa/models/
```

---

# Current Model Files

```text
aniwa/models/
├── enums.py
├── profile.py
```

Future versions may include:

```text
quality.py
statistics.py
schema.py
insights.py
lineage.py
governance.py
```

---

# Primary Model: DatasetProfile

The most important model in Aniwa.

Represents the full profiling result.

Conceptual structure:

```python
DatasetProfile(
    summary=...,
    columns=...,
    quality=...,
    insights=...,
    metadata=...
)
```

---

# Purpose of DatasetProfile

Acts as the:

- central profiling container
- reporting input
- serialization layer
- system integration object

All report generators consume this model.

---

# DatasetProfile Flow

```text
dataset
→ profiler engine
→ DatasetProfile
→ report renderer
```

---

# DatasetSummary Model

Represents high-level dataset information.

Typical fields:

```python
rows
columns
```

Future fields may include:

```python
memory_usage
compression_ratio
estimated_cost
health_score
```

---

# Purpose of DatasetSummary

Provides:

- quick overview
- dashboard statistics
- lightweight inspection
- report card generation

---

# ColumnProfile Model

Represents individual column analysis.

Typical fields:

```python
name
dtype
null_count
null_percent
unique_count
numeric_stats
```

---

# Purpose of ColumnProfile

Tracks:

- schema information
- data quality
- cardinality
- statistical analysis

Each dataset column maps to one ColumnProfile.

---

# ColumnProfile Flow

```text
dataset column
→ column analysis
→ ColumnProfile
→ report rendering
```

---

# NumericStatistics Model

Represents numeric analysis.

Typical fields:

```python
min
max
mean
median
std
```

---

# Purpose of NumericStatistics

Provides:

- quantitative analysis
- distribution understanding
- statistical insights
- anomaly visibility

---

# Future Numeric Statistics

Future versions may include:

```python
variance
quantiles
iqr
skewness
kurtosis
histograms
percentiles
```

---

# QualityProfile Model

Represents dataset quality information.

Typical fields:

```python
duplicate_rows
duplicate_percent
```

---

# Purpose of QualityProfile

Tracks:

- duplication
- quality degradation
- trust indicators
- future governance signals

---

# Future Quality Metrics

Future systems may include:

```python
consistency_scores
validation_failures
outlier_counts
missing_patterns
schema_drift
trust_scores
```

---

# Insight Model

Represents intelligent profiling observations.

Typical fields:

```python
level
message
```

---

# Purpose of Insights

Provides:

- warnings
- recommendations
- anomaly detection
- intelligent interpretation

---

# Insight Levels

Current levels:

```python
info
warning
critical
```

---

# Insight Flow

```text
profiling analysis
→ rule engine
→ Insight model
→ report display
```

---

# ProfileMetadata Model

Tracks profiling execution metadata.

Typical fields:

```python
generated_at
aniwa_version
python_version
operating_system
dataset_path
dataset_size
profiling_mode
report_format
```

---

# Purpose of Metadata

Provides:

- reproducibility
- auditing
- debugging
- operational traceability

---

# Metadata Importance

Metadata becomes critical for:

- enterprise governance
- compliance
- CI/CD
- audit trails
- profiling history

---

# Metadata Flow

```text
CLI execution
→ environment inspection
→ metadata generation
→ report embedding
```

---

# Model Relationships

Current relationships:

```text
DatasetProfile
├── DatasetSummary
├── ColumnProfile[]
├── QualityProfile
├── Insight[]
└── ProfileMetadata
```

---

# Why Centralized Models Matter

Centralized models create:

- consistent reporting
- easier testing
- cleaner serialization
- safer refactoring
- scalable integrations

---

# Serialization Support

Models are designed for:

- JSON export
- report rendering
- API systems
- future cloud workflows

---

# JSON Compatibility

Aniwa models are intentionally JSON-friendly.

Benefits:

- portability
- integrations
- APIs
- machine-readable outputs

---

# Model Validation Philosophy

Aniwa prioritizes:

- explicit structures
- safe defaults
- typed workflows
- predictable outputs

---

# Type Safety

Strong typing improves:

- developer experience
- IDE support
- maintainability
- scalability
- refactoring safety

---

# Future Pydantic Expansion

Future systems may fully adopt:

```python
Pydantic v2
```

for:

- validation
- serialization
- API generation
- schema generation

---

# Potential Future Model Structure

Possible future organization:

```text
models/
├── core/
├── statistics/
├── quality/
├── governance/
├── lineage/
├── ai/
└── connectors/
```

---

# Future Governance Models

Future governance systems may include:

```python
TrustScore
ComplianceResult
LineageGraph
PolicyViolation
```

---

# Future AI Models

Possible future AI models:

```python
SemanticSummary
DatasetIntent
AnomalyExplanation
Recommendation
```

---

# Future Lineage Models

Possible future lineage systems:

```python
DatasetNode
TransformationStep
SourceReference
DependencyGraph
```

---

# Enterprise Scaling Vision

At enterprise scale, models become the backbone for:

- APIs
- orchestration systems
- governance engines
- distributed profiling
- cloud infrastructure

---

# Long-Term Model Philosophy

Aniwa models should remain:

- modular
- explicit
- extensible
- interoperable
- stable

even as the platform grows significantly.

---

# Internal Architectural Importance

Models separate:

```text
profiling logic
from
presentation logic
```

This is extremely important.

---

# Why Separation Matters

Without separation:

- reports become tightly coupled
- APIs become fragile
- refactoring becomes dangerous

Models create architectural stability.

---

# Report Independence

Because of models:

- HTML reports
- PDF reports
- JSON reports
- console reports

all consume the same structures.

This dramatically improves maintainability.

---

# Testing Benefits

Models improve testing by enabling:

- deterministic outputs
- snapshot testing
- isolated validation
- serialization checks

---

# Example Testing Flow

```text
dataset
→ DatasetProfile
→ assert expected values
```

instead of testing UI directly.

---

# Future API Systems

Future REST or GraphQL APIs will likely expose models directly.

Example:

```json
{
  "summary": {...},
  "quality": {...},
  "insights": [...]
}
```

---

# Future Distributed Systems

Future distributed profiling systems may pass models between:

- workers
- queues
- orchestration engines
- storage systems

---

# Best Practices

---

## Keep Models Focused

Each model should represent one concept.

---

## Avoid Business Logic in Models

Models should primarily store structured data.

---

## Prefer Explicit Fields

Avoid ambiguous structures.

Bad:

```python
data = {}
```

Better:

```python
summary = DatasetSummary(...)
```

---

## Keep Models Serializable

Future systems depend on portability.

---

# Common Mistakes

---

## Mixing Rendering Into Models

Bad architecture:

```python
model.render_html()
```

Rendering should remain separate.

---

## Using Untyped Dictionaries Everywhere

Typed models are safer.

---

## Creating Overly Large Models

Prefer modular composition.

---

# Future Architectural Evolution

Models will eventually support:

- distributed profiling
- streaming systems
- AI enrichment
- governance engines
- observability platforms
- enterprise integrations

---

# Long-Term Vision

Over the next decade, Aniwa's models may evolve into:

- organization-wide profiling schemas
- universal data quality contracts
- semantic intelligence structures
- AI-native dataset representations

---

# Summary

Aniwa models provide:

- structured profiling outputs
- scalable architecture
- report consistency
- type safety
- serialization support
- future extensibility

Models are one of the core foundations of Aniwa's architecture.

---

# Related Documentation

Continue with:

- architecture/core-engine.md
- architecture/reporting-system.md
- architecture/cli.md
- api/profiler.md