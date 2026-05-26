# Profiling Modes

Aniwa supports multiple profiling modes designed for different performance, scalability, and analysis requirements.

Profiling modes determine:

- profiling depth
- computational intensity
- analysis completeness
- execution speed
- statistical coverage

---

# Available Modes

Aniwa currently supports:

- fast
- deep

---

# Fast Mode

Fast mode is optimized for speed and lightweight dataset inspection.

Example:

```bash
aniwa dataset.csv --mode fast
```

---

# Fast Mode Goals

Fast mode prioritizes:

- rapid execution
- lightweight profiling
- minimal memory overhead
- fast feedback loops

---

# Fast Mode Use Cases

Fast mode is ideal for:

- CI/CD validation
- quick inspections
- debugging pipelines
- exploratory checks
- very large datasets
- development workflows

---

# Fast Mode Characteristics

Fast mode generally performs:

- lightweight schema analysis
- basic null detection
- duplicate analysis
- limited statistics
- lightweight insights

Fast mode avoids:

- expensive computations
- deep statistical analysis
- heavy cardinality analysis
- complex heuristics

---

# Example Fast Workflow

```bash
aniwa production.csv --mode fast
```

Typical usage:

```bash
aniwa production.csv \
  --mode fast \
  --report json
```

---

# Deep Mode

Deep mode performs comprehensive dataset profiling.

Example:

```bash
aniwa dataset.csv --mode deep
```

---

# Deep Mode Goals

Deep mode prioritizes:

- profiling completeness
- statistical richness
- intelligent analysis
- dataset understanding

---

# Deep Mode Use Cases

Deep mode is ideal for:

- audits
- governance
- data onboarding
- quality validation
- production reviews
- reporting workflows

---

# Deep Mode Characteristics

Deep mode performs:

- full schema profiling
- comprehensive quality analysis
- detailed statistics
- intelligent heuristics
- insight generation
- richer metadata collection

---

# Deep Mode Example

```bash
aniwa production.csv \
  --mode deep \
  --report pdf
```

---

# Internal Architecture

Profiling mode logic is primarily handled in:

```text
aniwa/core/profiler.py
aniwa/cli.py
```

---

# Runtime Flow

Internally:

```text
CLI
→ resolve mode
→ profiler execution
→ mode-aware profiling
→ report generation
```

---

# Performance Philosophy

Aniwa profiling modes are designed around:

- scalability
- flexibility
- developer experience
- operational efficiency

---

# Tradeoffs

---

## Fast Mode

Advantages:

- faster execution
- lower memory usage
- ideal for automation

Disadvantages:

- reduced analytical depth
- fewer insights
- less statistical coverage

---

## Deep Mode

Advantages:

- richer analysis
- more intelligent insights
- better auditing support

Disadvantages:

- slower execution
- more computational work
- higher memory usage

---

# Recommended Usage

---

## Use Fast Mode For

- CI pipelines
- pre-validation
- large datasets
- exploratory work
- development loops

Example:

```bash
aniwa dataset.csv --mode fast
```

---

## Use Deep Mode For

- production validation
- governance workflows
- executive reporting
- dataset onboarding
- compliance reviews

Example:

```bash
aniwa dataset.csv --mode deep
```

---

# Mode Resolution

Mode resolution follows:

```text
CLI argument
→ config value
→ default value
```

Default mode:

```text
deep
```

---

# Configuration Example

```yaml
mode: deep
```

Override:

```bash
aniwa dataset.csv --mode fast
```

---

# Mode-Aware Insights

Future versions of Aniwa may generate:

- lightweight insights in fast mode
- advanced semantic insights in deep mode

---

# Future Profiling Modes

Planned future modes may include:

---

## Streaming Mode

For massive datasets:

```text
stream
```

Potential features:

- chunked processing
- incremental profiling
- low-memory execution

---

## Distributed Mode

For distributed compute systems:

```text
distributed
```

Potential integrations:

- Spark
- Ray
- Dask

---

## AI Mode

AI-assisted profiling:

```text
ai
```

Potential capabilities:

- semantic understanding
- anomaly explanations
- natural language summaries

---

# Scalability Strategy

Long-term scalability goals include:

- lazy execution
- vectorized analysis
- chunked computation
- parallel profiling
- adaptive heuristics

---

# Internal Design Philosophy

Profiling modes are intentionally:

- extensible
- modular
- configurable
- future-proof

This allows Aniwa to evolve without redesigning the CLI architecture.

---

# Example Enterprise Workflow

---

## CI Validation

```bash
aniwa dataset.csv --mode fast
```

---

## Governance Audit

```bash
aniwa dataset.csv \
  --mode deep \
  --report pdf \
  --template enterprise
```

---

# Best Practices

Recommended practices:

- use fast mode in automation
- use deep mode in audits
- standardize modes across teams
- benchmark large datasets
- profile incrementally when possible

---

# Common Mistakes

---

## Using Deep Mode in CI

Deep mode may increase runtime unnecessarily.

Use:

```bash
--mode fast
```

for CI pipelines.

---

## Using Fast Mode for Governance

Fast mode may skip deeper analysis.

Use:

```bash
--mode deep
```

for audits and validation.

---

# Future Vision

Long-term profiling architecture aims to support:

- adaptive profiling
- workload-aware execution
- intelligent optimization
- distributed intelligence
- metadata-driven profiling
- semantic understanding

---

# Next Steps

Continue with:

- report-formats.md
- report-templates.md
- sections.md
- charts.md