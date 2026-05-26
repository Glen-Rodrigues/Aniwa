# First Profile

This guide explains what happens internally when you run your first Aniwa profile.

---

# Basic Profiling

Run:

```bash
aniwa examples/customers.csv
```

Aniwa automatically:

1. validates the dataset path
2. detects dataset type
3. loads the dataset
4. profiles schema information
5. analyzes quality
6. calculates statistics
7. generates insights
8. renders a report

---

# What Aniwa Detects

Aniwa analyzes:

- dataset dimensions
- column names
- data types
- missing values
- duplicate rows
- uniqueness
- numeric distributions
- suspicious patterns
- potential IDs
- potential sensitive information

---

# Example Dataset

Example:

```csv
customer_id,name,email,country,revenue
1,Ama,ama@test.com,Ghana,200
2,Kojo,kojo@test.com,Ghana,150
3,Esi,,Nigeria,300
4,Kwame,kwame@test.com,Ghana,120
4,Kwame,kwame@test.com,Ghana,120
```

---

# Example Console Report

```text
Dataset Summary
Rows: 5
Columns: 5

Column Profile
customer_id | Int64
name        | String
email       | String

Insights
- duplicate rows detected
- possible sensitive information detected
```

---

# Understanding Sections

Aniwa reports are divided into sections.

---

## Summary

Provides:

- total rows
- total columns
- dataset dimensions

---

## Schema

Provides:

- column names
- inferred data types
- structural overview

---

## Quality

Provides:

- null analysis
- duplicate detection
- uniqueness analysis

---

## Statistics

Provides:

- min
- max
- mean
- median
- standard deviation

---

## Insights

Provides intelligent warnings including:

- sparse columns
- duplicate rows
- suspicious patterns
- possible IDs
- potential sensitive columns

---

# Fast vs Deep Profiling

---

## Fast Mode

```bash
aniwa examples/customers.csv --mode fast
```

Fast mode prioritizes:

- speed
- lightweight checks
- quick exploration

---

## Deep Mode

```bash
aniwa examples/customers.csv --mode deep
```

Deep mode prioritizes:

- completeness
- deeper statistics
- intelligent analysis

---

# Profiling Different File Types

---

## CSV

```bash
aniwa dataset.csv
```

---

## Excel

```bash
aniwa dataset.xlsx
```

---

## JSON

```bash
aniwa dataset.json
```

---

## Parquet

```bash
aniwa dataset.parquet
```

---

# Generating Reports

---

## HTML Report

```bash
aniwa examples/customers.csv \
  --report html \
  --output profile.html
```

---

## PDF Report

```bash
aniwa examples/customers.csv \
  --report pdf \
  --output profile.pdf
```

---

## Markdown Report

```bash
aniwa examples/customers.csv \
  --report markdown \
  --output profile.md
```

---

# Using Templates

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

# Understanding Insights

Insights are heuristic-based warnings generated from profiling logic.

Examples include:

---

## Duplicate Detection

```text
1 duplicate rows detected.
```

---

## Sparse Columns

```text
Column 'email' contains many null values.
```

---

## Sensitive Information Detection

```text
Column 'email' may contain sensitive information.
```

---

# Metadata Tracking

Aniwa also records profiling metadata including:

- profiling duration
- report format
- template used
- command executed
- dataset size
- operating system
- Python version
- Aniwa version

This improves:

- reproducibility
- auditing
- debugging
- automation

---

# Recommended Beginner Workflow

Recommended first workflow:

```bash
aniwa dataset.csv
```

Then:

```bash
aniwa dataset.csv --report html
```

Then:

```bash
aniwa dataset.csv --report pdf --template enterprise
```

Finally:

```bash
aniwa dataset.csv --mode deep
```

---

# Common Beginner Mistakes

---

## Wrong File Path

Incorrect:

```bash
aniwa customers.csv
```

Correct:

```bash
aniwa examples/customers.csv
```

---

## Unsupported File Type

Aniwa currently supports:

- CSV
- Excel
- JSON
- Parquet

---

## Missing Dependencies

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Next Steps

Continue with:

- configuration.md
- report-formats.md
- profiling-modes.md
- cli-reference.md