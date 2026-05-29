# Modes & Presets

## Overview

Aniwa provides two powerful ways to control profiling behavior: **modes** and **presets**. While they work together, they serve different purposes:

- **Modes** control how intensive the profiling process is
- **Presets** control complete profiling workflows including mode, report format, sections, and more

Think of modes as the "engine" and presets as the "package" that configures everything for specific use cases.

## Profiling Modes

Modes determine the depth and intensity of the profiling analysis.

### Fast Mode (`--mode fast`)

Lightweight profiling optimized for speed. Perfect for quick checks and large datasets.

**Includes**:
- Schema detection
- Null value analysis
- Duplicate detection
- Basic quality metrics

**Excludes**:
- Statistical computations (mean, median, std, etc.)
- Advanced insights
- Correlation analysis
- Chart generation

**Best for**:
- Initial data exploration
- CI/CD pipelines
- Very large datasets (>1M rows)
- When you only need basic structure

**Example**:
```bash
aniwa profile customers.csv --mode fast
```

### Deep Mode (`--mode deep`)

Comprehensive profiling with full statistical analysis. This is the default mode.

**Includes everything from fast mode plus**:
- Statistical summaries (min, max, mean, median, std)
- Distribution analysis
- Advanced insights
- Pattern detection
- Correlation analysis (future)

**Best for**:
- Detailed data understanding
- Quality assessment
- Data science preparation
- Audit and compliance

**Example**:
```bash
aniwa profile customers.csv --mode deep
```

## Profiling Presets

Presets are complete workflow configurations that combine multiple settings including mode, report format, sections, and verbosity.

### Quick Preset (`--preset quick`)

Fast, lightweight profiling for quick data inspection.

**Configuration**:
| Setting | Value |
|---------|-------|
| Mode | fast |
| Sections | summary, schema, quality |
| Report Format | console |
| Verbosity | normal |

**Use case**: Initial data exploration, CI/CD pipelines

**Example**:
```bash
aniwa profile customers.csv --preset quick
```

### Standard Preset (`--preset standard`)

Balanced default profiling with statistics and insights.

**Configuration**:
| Setting | Value |
|---------|-------|
| Mode | deep |
| Sections | summary, schema, quality, statistics, insights |
| Report Format | console |
| Verbosity | normal |

**Use case**: Daily profiling tasks, general analysis

**Example**:
```bash
aniwa profile customers.csv --preset standard
```

### Audit Preset (`--preset audit`)

Comprehensive profiling for validation and audit workflows.

**Configuration**:
| Setting | Value |
|---------|-------|
| Mode | deep |
| Sections | all sections |
| Report Format | html |
| Template | enterprise |
| Verbosity | verbose |

**Use case**: Compliance, detailed documentation, audit trails

**Example**:
```bash
aniwa profile customers.csv --preset audit
```

### Enterprise Preset (`--preset enterprise`)

Professional branded reporting for stakeholders.

**Configuration**:
| Setting | Value |
|---------|-------|
| Mode | deep |
| Sections | all sections |
| Report Format | html |
| Template | enterprise |
| Verbosity | normal |

**Use case**: Executive reports, client deliverables

**Example**:
```bash
aniwa profile customers.csv --preset enterprise
```

## Modes vs Presets Comparison

| Aspect | Modes | Presets |
|--------|-------|---------|
| **Controls** | Profiling intensity only | Complete workflow |
| **Settings** | Single setting | Multiple settings |
| **Flexibility** | Low (2 options) | High (composable) |
| **Complexity** | Simple | Moderate |
| **Best for** | Quick adjustments | Complete workflows |

## Usage Guide

### Using Modes Alone

When you only need to control profiling depth:

```bash
# Fast mode for quick checks
aniwa profile data.csv --mode fast

# Deep mode for detailed analysis (default)
aniwa profile data.csv --mode deep
```

### Using Presets Alone

When you want complete pre-configured workflows:

```bash
# Quick inspection
aniwa profile data.csv --preset quick

# Standard analysis
aniwa profile data.csv --preset standard

# Audit preparation
aniwa profile data.csv --preset audit

# Professional report
aniwa profile data.csv --preset enterprise
```

### Combining Modes and Presets

Presets already include mode settings, but you can override them:

```bash
# Override preset mode
aniwa profile data.csv --preset quick --mode deep

# Override preset with different mode
aniwa profile data.csv --preset enterprise --mode fast
```

### Complete Examples with Other Options

```bash
# Preset + output directory
aniwa profile data.csv --preset enterprise --output-dir ./reports

# Mode + specific sections
aniwa profile data.csv --mode deep --include statistics,insights

# Preset + format override
aniwa profile data.csv --preset audit --report json

# Preset + verbosity override
aniwa profile data.csv --preset audit --verbosity quiet

# Everything together
aniwa profile data.csv \
    --preset enterprise \
    --mode fast \
    --output-dir ./reports \
    --template dark \
    --verbosity verbose
```

## Decision Matrix

Choose based on your needs:

| If you need... | Use... | Example |
|----------------|--------|---------|
| Quick structure check | `--mode fast` | `aniwa profile data.csv --mode fast` |
| Detailed statistics | `--mode deep` | `aniwa profile data.csv --mode deep` |
| Fast + specific sections | `--mode fast` with `--include` | `aniwa profile data.csv --mode fast --include statistics` |
| Professional report | `--preset enterprise` | `aniwa profile data.csv --preset enterprise` |
| Audit documentation | `--preset audit` | `aniwa profile data.csv --preset audit` |
| Daily analysis | `--preset standard` | `aniwa profile data.csv --preset standard` |
| CI/CD pipeline | `--preset quick --verbosity quiet` | `aniwa profile data.csv --preset quick --verbosity quiet` |
| Custom workflow | Mode + individual options | `aniwa profile data.csv --mode deep --report json --exclude charts` |

## Configuration Priority

When multiple configuration sources are used, priority is:

1. **CLI arguments** (highest) - Individual flags like `--mode`, `--report`, etc.
2. **Preset values** - When `--preset` is specified
3. **Configuration file** - From `aniwa.yaml`, `aniwa.yml`, `aniwa.toml`, or `aniwa.json`
4. **Defaults** (lowest) - Built-in defaults

### Priority Examples

```bash
# Preset overrides config file
aniwa profile data.csv --preset enterprise  # Uses preset values over config.yaml

# CLI overrides preset
aniwa profile data.csv --preset quick --mode deep  # Uses deep mode, not fast

# CLI overrides everything
aniwa profile data.csv --preset enterprise --mode fast --report json
```

## Listing Available Presets

View all built-in presets:

```bash
aniwa list-presets
```

Output:
```
┌──────────────┬──────────────────────────────────────────────┐
│ Preset       │ Description                                  │
├──────────────┼──────────────────────────────────────────────┤
│ quick        │ Fast lightweight profiling for quick data    │
│              │ inspection                                   │
│ standard     │ Balanced default profiling with statistics   │
│              │ and insights                                 │
│ audit        │ Comprehensive profiling for validation and   │
│              │ audit workflows                              │
│ enterprise   │ Professional branded reporting for           │
│              │ stakeholders                                 │
└──────────────┴──────────────────────────────────────────────┘
```

## Quick Reference Card

```bash
# MODES
--mode fast      # Lightweight, fast profiling
--mode deep      # Full analysis (default)

# PRESETS
--preset quick       # Fast + basic sections
--preset standard    # Deep + stats + insights
--preset audit       # Deep + all sections + HTML + verbose
--preset enterprise  # Deep + all sections + HTML

# LIST PRESETS
aniwa list-presets

# COMMON COMBINATIONS
aniwa profile data.csv --preset quick                    # Quick check
aniwa profile data.csv --preset standard                 # Daily use
aniwa profile data.csv --preset audit                    # Audit report
aniwa profile data.csv --preset enterprise               # Client report
aniwa profile data.csv --preset quick --mode deep        # Override mode
aniwa profile data.csv --preset audit --verbosity quiet  # Quiet audit
```

## Best Practices

### For Beginners
1. Start with `--preset quick` to understand your data structure
2. Move to `--preset standard` for deeper analysis
3. Use `--preset enterprise` when sharing reports with stakeholders

### For Daily Use
1. Use `--preset standard` as your default
2. Override with `--mode fast` for very large files
3. Add `--report html` when you need to save results

### For CI/CD Pipelines
```bash
# Quiet, fast, machine-readable
aniwa profile data.csv --preset quick --verbosity quiet --report json
```

### For Data Governance
```bash
# Comprehensive, documented, audit-ready
aniwa profile data.csv --preset audit --output-dir ./audits/$(date +%Y%m%d)
```

## Troubleshooting

### Issue: Profiling is too slow
**Solution**: Use fast mode or quick preset
```bash
aniwa profile large.csv --mode fast
# or
aniwa profile large.csv --preset quick
```

### Issue: Need more detailed statistics
**Solution**: Use deep mode or standard/audit preset
```bash
aniwa profile data.csv --mode deep
# or
aniwa profile data.csv --preset standard
```

### Issue: Preset not working as expected
**Solution**: Check priority and use debug mode
```bash
aniwa profile data.csv --preset enterprise --verbosity debug
```

### Issue: Want to see all available options
**Solution**: Use help
```bash
aniwa profile --help
aniwa list-presets
```

## Future Roadmap

### Planned Mode Enhancements
- **Turbo mode** - Even faster than fast for massive datasets
- **Sample mode** - Profile a sample of large datasets
- **Streaming mode** - Profile without loading entire dataset

### Planned Preset Enhancements
- **Custom presets** - User-defined in config files
- **Preset inheritance** - Extend existing presets
- **ML presets** - Specialized for machine learning workflows
- **Data quality presets** - Focus on data validation
- **Privacy presets** - PII detection and anonymization
- **Cloud presets** - Optimized for cloud data sources
