# Verbosity Levels

Aniwa provides multiple verbosity levels that control how much information is displayed during profiling.

Verbosity helps balance:

* output clarity
* troubleshooting visibility
* automation friendliness
* developer experience
* debugging support

---

# What is Verbosity?

Verbosity determines how much information Aniwa displays while processing datasets.

Higher verbosity levels provide more detailed insight into execution, while lower levels reduce console noise.

Aniwa currently supports:

* quiet
* normal
* verbose
* debug

---

# Quiet

Quiet mode minimizes console output.

Example:

```bash
aniwa profile dataset.csv --verbosity quiet
```

---

# Quiet Mode Goals

Quiet mode prioritizes:

* minimal output
* automation
* clean logs
* CI/CD pipelines

---

# Quiet Mode Characteristics

Quiet mode generally shows:

* critical errors
* final status information

Quiet mode hides:

* progress messages
* informational logs
* detailed execution messages

---

# Recommended Use Cases

Use quiet mode for:

* CI pipelines
* scheduled jobs
* batch processing
* automation workflows

---

# Normal

Normal mode provides balanced output for everyday usage.

Example:

```bash
aniwa profile dataset.csv --verbosity normal
```

---

# Normal Mode Goals

Normal mode prioritizes:

* usability
* readability
* useful feedback
* routine profiling

---

# Normal Mode Characteristics

Normal mode generally shows:

* important status messages
* progress updates
* summary information

---

# Recommended Use Cases

Use normal mode for:

* everyday profiling
* local development
* interactive terminal usage

---

# Verbose

Verbose mode provides additional operational detail.

Example:

```bash
aniwa profile dataset.csv --verbosity verbose
```

---

# Verbose Mode Goals

Verbose mode prioritizes:

* transparency
* troubleshooting
* execution visibility

---

# Verbose Mode Characteristics

Verbose mode generally shows:

* detailed processing steps
* additional status messages
* extended execution information

---

# Recommended Use Cases

Use verbose mode for:

* troubleshooting
* workflow validation
* understanding execution flow

---

# Debug

Debug mode provides maximum output detail.

Example:

```bash
aniwa profile dataset.csv --verbosity debug
```

---

# Debug Mode Goals

Debug mode prioritizes:

* diagnostics
* debugging
* development support

---

# Debug Mode Characteristics

Debug mode generally shows:

* debugging information
* internal execution details
* diagnostic messages

---

# Recommended Use Cases

Use debug mode for:

* bug investigations
* development
* issue reporting

---

# Comparison

| Level   | Detail Level | Best For                  |
| ------- | ------------ | ------------------------- |
| quiet   | Minimal      | Automation                |
| normal  | Standard     | Everyday usage            |
| verbose | Detailed     | Troubleshooting           |
| debug   | Maximum      | Development and debugging |

---

# Configuration Example

Verbosity can be configured in configuration files.

Example:

```yaml
verbosity: normal
```

Other supported values:

```yaml
verbosity: quiet
```

```yaml
verbosity: verbose
```

```yaml
verbosity: debug
```

---

# Resolution Priority

Verbosity resolution follows:

```text
CLI argument
- config value
- default value
```

Default verbosity:

```text
normal
```

---

# Testing Verbosity Levels

To compare verbosity levels, run:

```bash
aniwa profile examples/customers.csv --verbosity quiet
aniwa profile examples/customers.csv --verbosity normal
aniwa profile examples/customers.csv --verbosity verbose
aniwa profile examples/customers.csv --verbosity debug
```

Observe how output increases from minimal information in quiet mode to highly detailed diagnostic information in debug mode.

---

# Best Practices

Recommended practices:

* use quiet mode in automation
* use normal mode for everyday work
* use verbose mode for troubleshooting
* use debug mode when investigating issues

---

# Common Mistakes

## Using Debug Mode Everywhere

Debug mode can produce large amounts of output.

Use normal mode unless additional detail is required.

---

## Using Quiet Mode for Troubleshooting

Quiet mode hides useful execution information.

Use verbose or debug mode when diagnosing problems.

---

# Summary

Aniwa verbosity levels provide flexible control over console output.

Choose:

* quiet for automation
* normal for daily usage
* verbose for troubleshooting
* debug for diagnostics and development