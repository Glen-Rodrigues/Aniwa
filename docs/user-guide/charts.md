# Charts

Aniwa supports visual profiling charts to help users understand datasets faster through graphical analysis.

Charts transform raw profiling metrics into intuitive visual insights.

They improve:

- readability
- anomaly detection
- data exploration
- executive communication
- debugging workflows
- governance reporting

---

# Why Charts Matter

Raw tables become difficult to scan at scale.

Charts help users instantly identify:

- high-null columns
- cardinality spikes
- duplicate-heavy datasets
- unusual distributions
- structural imbalances

Visualization dramatically improves dataset comprehension.

---

# Current Chart Support

Aniwa currently supports:

| Chart | Purpose |
|---|---|
| Null Percentage Chart | visualize missing values |
| Unique Values Chart | visualize cardinality |
| Duplicate Overview Chart | visualize duplicate ratios |

---

# Supported Report Formats

Charts currently appear in:

- HTML reports
- PDF reports

Charts are not currently supported in:

- console reports
- JSON reports
- markdown reports

---

# Chart Architecture

Aniwa charts are generated using:

- Chart.js
- Jinja2 templates
- embedded JSON chart data

---

# Rendering Pipeline

Chart rendering flow:

```text
profile_dataframe()
→ dataset profile
→ chart data serialization
→ Jinja template
→ Chart.js rendering
→ final HTML/PDF
```

---

# Chart Data Serialization

Aniwa injects serialized chart data into templates.

Example:

```html
<script id="aniwa-chart-data" type="application/json">
{
    "columns": [...],
    "nullPercents": [...],
    "uniqueCounts": [...]
}
</script>
```

This allows frontend chart rendering without additional APIs.

---

# Null Percentage Chart

The null percentage chart visualizes missing values across columns.

Purpose:

- identify sparse columns
- detect ingestion issues
- locate incomplete fields

---

## Example Use Cases

Useful for:

- ETL debugging
- governance validation
- ML preprocessing
- schema validation

---

## Interpretation

High null percentages may indicate:

- missing source data
- optional fields
- ingestion failures
- schema mismatches

---

# Unique Values Chart

The unique values chart visualizes column cardinality.

Purpose:

- identify ID-like fields
- detect categorical imbalance
- understand uniqueness patterns

---

## Interpretation

High cardinality may indicate:

- IDs
- UUIDs
- emails
- hashes
- transaction references

Low cardinality may indicate:

- categories
- enums
- flags
- labels

---

# Duplicate Overview Chart

The duplicate chart visualizes:

- duplicate rows
- unique rows

Purpose:

- identify duplication severity
- evaluate dataset quality
- support governance checks

---

# Doughnut Chart Usage

Aniwa currently uses doughnut charts for duplicate visualization.

Reasoning:

- compact layout
- intuitive proportions
- visually clear comparison

---

# Chart.js Integration

Aniwa uses Chart.js because it provides:

- lightweight rendering
- responsive charts
- strong browser compatibility
- simple configuration
- modern visuals

---

# Why Frontend Rendering?

Aniwa renders charts client-side instead of pre-generating images.

Benefits:

- smaller reports
- interactive rendering
- responsive layouts
- reduced backend complexity

---

# Chart Responsiveness

Charts automatically adapt to:

- desktop screens
- tablets
- mobile devices

This is achieved using responsive Chart.js options.

---

# Example Responsive Config

```javascript
options: {
    responsive: true
}
```

---

# Chart Layout System

Aniwa uses CSS grid layouts for charts.

Example:

```css
.charts {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
```

This enables:

- balanced layouts
- responsive rendering
- scalable dashboard structures

---

# Full-Width Charts

Some charts span multiple columns.

Example:

```css
.chart-card.full {
    grid-column: 1 / -1;
}
```

Useful for:

- overview charts
- large visualizations
- executive summaries

---

# Chart Styling Philosophy

Aniwa charts prioritize:

- readability
- simplicity
- clarity
- performance
- accessibility

Charts should never overwhelm the report.

---

# Template-Specific Styling

Different templates apply different chart aesthetics.

Examples:

| Template | Style |
|---|---|
| clean | minimal |
| compact | dense |
| enterprise | polished |
| dark | dark-mode optimized |

---

# Dark Mode Charts

Dark templates customize:

- grid colors
- axis colors
- backgrounds
- datasets

Example:

```javascript
const darkAxis = "#cbd5e1";
```

---

# Chart Colors

Current charts use semantic color systems.

Examples:

| Meaning | Color |
|---|---|
| nulls | blue |
| duplicates | red |
| uniqueness | teal |
| warnings | yellow |

---

# Accessibility Considerations

Aniwa charts aim to support:

- high contrast
- readable labels
- color clarity
- scalable sizing

Future goals include:

- colorblind-safe palettes
- screen reader support
- WCAG compliance

---

# Chart Performance

Large datasets can impact rendering performance.

Potential bottlenecks:

- thousands of columns
- massive cardinality
- wide datasets

---

# Future Optimization Strategies

Potential future optimizations:

- lazy rendering
- chart pagination
- sampling
- virtualization
- WebGL rendering

---

# Future Planned Charts

Planned future visualizations include:

- correlation matrices
- histograms
- outlier plots
- drift visualizations
- distribution plots
- heatmaps
- embeddings
- semantic clusters

---

# Statistical Visualization Roadmap

Future numeric charts may include:

- box plots
- violin plots
- percentile distributions
- skewness visualization

---

# Governance Visualization Roadmap

Future governance charts may include:

- quality scoring
- trust metrics
- lineage graphs
- validation coverage

---

# AI Visualization Roadmap

Future AI-assisted visualizations may include:

- anomaly explanations
- semantic clustering
- natural language summaries
- automated chart recommendations

---

# Chart Section Control

Charts can be included or excluded.

Example:

```bash
aniwa dataset.csv \
  --exclude charts
```

---

# Template Rendering Conditions

Charts render conditionally.

Example:

```jinja2
{% if profile.columns %}
```

This prevents:

- empty charts
- invalid rendering
- broken layouts

---

# PDF Chart Rendering

PDF exports may render charts differently depending on renderer implementation.

Possible future architecture:

```text
Chart.js
→ HTML rendering
→ headless browser
→ PDF snapshot
```

---

# Interactive Chart Vision

Future HTML reports may support:

- zooming
- filtering
- hover analysis
- cross-highlighting
- drill-down interactions

---

# Enterprise Dashboard Vision

Long-term goals include transforming charts into full dashboards.

Possible future features:

- live monitoring
- historical comparisons
- profiling timelines
- governance scoring
- observability integrations

---

# Future Plugin System

Future architecture may support custom charts.

Example:

```text
aniwa/plugins/charts/
```

Allowing:

- custom visualizations
- domain-specific dashboards
- governance plugins
- ML visualizations

---

# Best Practices

---

## Avoid Overcrowding

Too many charts reduce readability.

---

## Focus on Actionable Insights

Charts should answer meaningful questions.

---

## Use Appropriate Templates

Examples:

| Workflow | Template |
|---|---|
| governance | enterprise |
| development | compact |
| presentations | clean |
| engineering | dark |

---

# Common Mistakes

---

## Assuming Charts Exist in Console Reports

Charts currently require HTML or PDF reports.

---

## Forgetting to Enable HTML Output

Incorrect:

```bash
aniwa dataset.csv --template dark
```

Correct:

```bash
aniwa dataset.csv \
  --report html \
  --template dark
```

---

# Long-Term Vision

Charts are foundational to Aniwa's long-term intelligence platform.

Future systems may evolve into:

- interactive dashboards
- profiling observability
- enterprise governance visualization
- AI-assisted data intelligence systems

---

# Summary

Aniwa charts provide:

- rapid visual understanding
- actionable insights
- governance visibility
- developer-friendly analytics
- scalable visualization architecture

They are a core part of making Aniwa:

> beautiful, intelligent, and developer-first.

---

# Next Steps

Continue with:

- metadata.md
- configuration.md
- profiling-modes.md
- output-formats.md