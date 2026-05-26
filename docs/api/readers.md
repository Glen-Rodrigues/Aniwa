# Readers API

The Readers API is responsible for loading datasets into Aniwa.

It acts as the ingestion layer between:

- external datasets
- internal dataframe systems
- profiling engines

The readers system is one of the foundational architectural layers of Aniwa.

---

# Purpose of the Readers System

The readers layer solves several critical problems:

- dataset format abstraction
- unified dataframe loading
- file validation
- scalable ingestion
- future connector extensibility

---

# High-Level Architecture

```text
dataset file
→ reader detection
→ format parser
→ Polars DataFrame
→ profiler
```

---

# Current Reader Location

```text
aniwa/io/readers.py
```

---

# Core Reader Philosophy

Aniwa readers are designed to be:

- universal
- extensible
- fast
- predictable
- format-agnostic
- scalable

---

# Current Supported Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| CSV | .csv |
| JSON | .json |
| Excel | .xlsx / .xls |
| Parquet | .parquet |

---

# Why Reader Abstraction Matters

Without abstraction:

- profiling logic becomes tightly coupled
- adding formats becomes difficult
- architecture becomes fragile

Reader abstraction separates ingestion from profiling.

---

# Current Reader Flow

```text
input path
→ extension detection
→ format-specific loader
→ Polars DataFrame
```

---

# Main Reader Entry Point

Core function:

```python
read_dataset(path)
```

This acts as the universal dataset loader.

---

# Reader Responsibilities

The readers system currently handles:

- file extension detection
- parser routing
- dataframe loading
- unsupported format handling
- ingestion normalization

---

# Reader Output

All readers return:

```python
Polars DataFrame
```

This standardization is extremely important.

---

# Why Standardized Outputs Matter

Standardized outputs enable:

- simpler profiler logic
- consistent pipelines
- report portability
- future scalability

---

# Current Reader Architecture

Conceptual structure:

```text
read_dataset()
├── read_csv()
├── read_json()
├── read_excel()
└── read_parquet()
```

---

# CSV Reader

CSV is currently one of the most common ingestion paths.

Example:

```bash
aniwa customers.csv
```

---

# CSV Flow

```text
.csv file
→ Polars CSV parser
→ DataFrame
```

---

# CSV Benefits

CSV support provides:

- universal compatibility
- lightweight ingestion
- interoperability

---

# JSON Reader

JSON support enables profiling of:

- API exports
- NoSQL exports
- event data
- machine-generated datasets

---

# JSON Flow

```text
.json file
→ JSON parser
→ DataFrame
```

---

# Excel Reader

Aniwa supports:

- .xlsx
- .xls

---

# Why Excel Matters

Excel remains extremely important because many organizations still rely heavily on spreadsheets.

Excel support is essential for:

- analysts
- business users
- operations teams
- non-technical workflows

---

# Excel Flow

```text
Excel file
→ Excel parser
→ DataFrame
```

---

# Parquet Reader

Parquet support enables:

- analytics workflows
- data lake workflows
- big data interoperability
- cloud-native datasets

---

# Why Parquet Matters

Parquet is critical for modern data engineering ecosystems.

It provides:

- columnar storage
- compression
- scalability
- high-performance analytics

---

# Parquet Flow

```text
.parquet file
→ Parquet parser
→ DataFrame
```

---

# Extension Detection

Aniwa determines reader behavior using:

```python
Path(path).suffix
```

---

# Extension Routing

Example:

```python
if suffix == ".csv":
```

This routes the dataset to the appropriate loader.

---

# Unsupported Format Handling

Unsupported formats produce:

```text
DatasetReadError
```

or equivalent validation errors.

---

# Why Explicit Errors Matter

Clear errors improve:

- developer experience
- debugging
- automation reliability

---

# Validation Philosophy

Readers validate:

- file existence
- supported extensions
- parsing success
- compatibility

---

# Internal Reader Design Philosophy

Readers should remain:

- lightweight
- focused
- composable
- isolated
- extensible

---

# Separation of Concerns

Readers should NOT contain:

- profiling logic
- report generation
- visualization logic
- intelligence systems

Their responsibility is ingestion only.

---

# Why Separation Matters

This separation enables:

- cleaner architecture
- easier testing
- scalable ingestion systems
- future connectors

---

# Current Scalability Model

Readers currently scale through:

- Polars optimizations
- efficient parsing
- columnar loading

---

# Future Reader Scalability

Future versions may support:

- streaming ingestion
- chunked loading
- distributed ingestion
- lazy evaluation

---

# Chunked Reading Vision

Future architecture may support:

```text
large dataset
→ chunk loading
→ incremental profiling
```

for memory efficiency.

---

# Streaming Reader Vision

Future streaming systems may support:

- Kafka
- Kinesis
- event streams
- real-time pipelines

---

# Database Reader Vision

Future connectors may include:

| System |
|---|
| PostgreSQL |
| MySQL |
| DuckDB |
| SQLite |
| Snowflake |
| BigQuery |
| Redshift |

---

# Cloud Storage Vision

Future ingestion systems may support:

- S3
- GCS
- Azure Blob Storage
- Lakehouse systems

---

# API Reader Vision

Future readers may ingest directly from:

- REST APIs
- GraphQL APIs
- webhooks
- event systems

---

# Data Lake Vision

Future ingestion systems may support:

- Delta Lake
- Iceberg
- Hudi
- LakeFS

---

# Enterprise Reader Vision

Enterprise ingestion may eventually support:

- schema registries
- lineage systems
- governance policies
- access controls
- distributed storage

---

# Reader Extensibility

Aniwa is intentionally designed to support new readers easily.

---

# Future Reader Plugin Architecture

Future plugin systems may allow:

```python
register_reader(".custom", custom_reader)
```

---

# Universal Ingestion Vision

Long-term vision:

```text
Any dataset
→ readable by Aniwa
```

regardless of source or format.

---

# Internal Reader Error Handling

Current philosophy:

```text
fail clearly
fail predictably
fail safely
```

---

# Reader Testing Philosophy

Readers are heavily tested because ingestion is foundational.

---

# Current Reader Tests

Reader tests validate:

- supported formats
- invalid paths
- unsupported formats
- parsing correctness
- dataframe integrity

---

# Example Reader Test Flow

```text
input file
→ read_dataset()
→ validate DataFrame
```

---

# Reader Performance Philosophy

Aniwa prioritizes:

- low memory usage
- fast loading
- scalable parsing
- efficient dataframe creation

---

# Why Polars Is Strategic

Polars enables future scalability because it supports:

- lazy execution
- parallelism
- vectorization
- Arrow interoperability

---

# Future Arrow Vision

Future systems may deeply integrate:

```text
Apache Arrow
```

for:

- zero-copy operations
- interoperability
- distributed systems

---

# Future Distributed Ingestion

Future enterprise systems may ingest datasets from:

- distributed filesystems
- cloud warehouses
- object stores
- orchestration systems

---

# Security Considerations

Future readers may require:

- authentication
- secrets management
- encrypted connections
- governance enforcement

---

# Best Practices

---

## Keep Readers Focused

Readers should only load datasets.

---

## Standardize Outputs

Always return consistent dataframe structures.

---

## Isolate Format Logic

Avoid mixing format-specific logic.

---

## Prefer Explicit Validation

Fail early when formats are unsupported.

---

# Common Mistakes

---

## Mixing Profiling Into Readers

Bad architecture:

```python
read_and_profile()
```

Readers should only ingest.

---

## Returning Multiple Data Types

Consistency matters.

Always return:

```python
Polars DataFrame
```

---

## Tight Coupling

Avoid tightly coupling readers to specific reports.

---

# Long-Term Architectural Role

Readers are the gateway into Aniwa.

Everything begins with ingestion.

Without robust readers:

- profiling fails
- scalability breaks
- enterprise adoption becomes difficult

---

# Summary

Aniwa's Readers API provides:

- universal dataset ingestion
- format abstraction
- scalable loading
- standardized dataframe outputs
- extensible architecture
- future connector support

The readers layer is foundational infrastructure for the entire platform.

---

# Related Documentation

Continue with:

- architecture/core-engine.md
- architecture/io-system.md
- api/profiler.md
- api/models.md