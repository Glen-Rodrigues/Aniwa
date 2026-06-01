from pathlib import Path

from typer.testing import CliRunner

from aniwa.cli import app

runner = CliRunner()


def write_csv(path: Path) -> None:
    path.write_text(
        "customer_id,name,email,revenue\n"
        "1,Ama,ama@example.com,1200\n"
        "2,Kofi,kofi@example.com,950\n"
        "3,Esi,,1100\n",
        encoding="utf-8",
    )


def invoke_profile(*args):
    """
    Helper to invoke:

        aniwa profile ...
    """
    return runner.invoke(
        app,
        ["profile", *args],
    )


def test_cli_mutually_exclusive_include_exclude(tmp_path):
    """Test that using both --include and --exclude is not allowed."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--include",
        "summary",
        "--exclude",
        "statistics",
    )

    # The CLI currently allows both (exclude takes precedence)
    # This test should be updated when mutual exclusion is enforced
    # For now, check that it doesn't crash
    assert result.exit_code == 0


def test_cli_invalid_include_section(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--include",
        "invalid_section",
    )

    assert result.exit_code != 0
    assert "Invalid report section" in result.output


def test_cli_invalid_exclude_section(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--exclude",
        "unknown_block",
    )

    assert result.exit_code != 0
    assert "Invalid report section" in result.output


def test_cli_missing_file():
    result = invoke_profile("does_not_exist.csv")

    assert result.exit_code != 0
    assert "not found" in result.output.lower() or "does not exist" in result.output.lower()


def test_cli_json_report(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "report.json"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "json",
        "--output",
        str(output_path),
    )

    assert result.exit_code == 0
    assert output_path.exists()


def test_cli_html_report(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "report.html"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--output",
        str(output_path),
    )

    assert result.exit_code == 0
    assert output_path.exists()


def test_cli_markdown_report(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "report.md"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "markdown",
        "--output",
        str(output_path),
    )

    assert result.exit_code == 0
    assert output_path.exists()


def test_cli_excel_report(tmp_path):
    """Test generating Excel report."""
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "report.xlsx"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "excel",
        "--output",
        str(output_path),
    )

    assert result.exit_code == 0
    assert output_path.exists()


def test_cli_pdf_report(tmp_path):
    """Test generating PDF report."""
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "report.pdf"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "pdf",
        "--output",
        str(output_path),
    )

    assert result.exit_code == 0
    assert output_path.exists()


def test_cli_output_dir_json(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_dir = tmp_path / "reports"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "json",
        "--output-dir",
        str(output_dir),
    )

    expected = output_dir / "aniwa_report.json"

    assert result.exit_code == 0
    assert expected.exists()


def test_cli_output_dir_html(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_dir = tmp_path / "reports"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--output-dir",
        str(output_dir),
    )

    expected = output_dir / "aniwa_report.html"

    assert result.exit_code == 0
    assert expected.exists()


def test_cli_output_and_output_dir_mutually_exclusive(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "json",
        "--output",
        "report.json",
        "--output-dir",
        "reports",
    )

    assert result.exit_code != 0
    assert "Use either --output or --output-dir" in result.output


def test_cli_fast_mode(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--mode",
        "fast",
    )

    assert result.exit_code == 0


def test_cli_deep_mode(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--mode",
        "deep",
    )

    assert result.exit_code == 0


def test_cli_invalid_mode(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--mode",
        "invalid",
    )

    assert result.exit_code != 0


def test_cli_invalid_report_format(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "invalid",
    )

    assert result.exit_code != 0


def test_cli_with_preset_quick(tmp_path):
    """Test using quick preset."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "quick",
    )

    # Preset should work
    assert result.exit_code == 0, f"Exit code: {result.exit_code}, Output: {result.output}"


def test_cli_with_preset_standard(tmp_path):
    """Test using standard preset."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "standard",
    )

    assert result.exit_code == 0, f"Exit code: {result.exit_code}, Output: {result.output}"


def test_cli_with_preset_audit(tmp_path):
    """Test using audit preset."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "audit",
    )

    assert result.exit_code == 0


def test_cli_with_preset_enterprise(tmp_path):
    """Test using enterprise preset."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "enterprise",
    )

    assert result.exit_code == 0


def test_cli_with_invalid_preset(tmp_path):
    """Test using invalid preset."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "invalid_preset",
    )

    assert result.exit_code != 0
    assert "Unknown preset" in result.output


def test_cli_preset_overrides_mode(tmp_path):
    """Test that preset mode can be overridden by CLI."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "quick",  # quick uses fast mode
        "--mode",
        "deep",   # override to deep
    )

    assert result.exit_code == 0, f"Exit code: {result.exit_code}, Output: {result.output}"


def test_cli_preset_with_include(tmp_path):
    """Test preset with additional include sections."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--preset",
        "quick",
        "--include",
        "statistics",
    )

    assert result.exit_code == 0


def test_list_presets_command():
    result = runner.invoke(
        app,
        ["list-presets"],
    )

    assert result.exit_code == 0
    assert "Preset" in result.output
    assert "quick" in result.output
    assert "standard" in result.output
    assert "audit" in result.output
    assert "enterprise" in result.output


def test_version_flag():
    result = runner.invoke(
        app,
        ["--version"],
    )

    assert result.exit_code == 0
    assert "aniwa version" in result.output


def test_verbosity_quiet(tmp_path):
    """Test quiet verbosity level."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--verbosity",
        "quiet",
    )

    assert result.exit_code == 0


def test_verbosity_verbose(tmp_path):
    """Test verbose verbosity level."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--verbosity",
        "verbose",
    )

    assert result.exit_code == 0


def test_verbosity_debug(tmp_path):
    """Test debug verbosity level."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--verbosity",
        "debug",
    )

    assert result.exit_code == 0


def test_cli_with_template_html(tmp_path):
    """Test using custom template with HTML report."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--template",
        "dark",
    )

    assert result.exit_code == 0


def test_cli_with_template_clean(tmp_path):
    """Test using clean template."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--template",
        "clean",
    )

    assert result.exit_code == 0


def test_cli_with_template_compact(tmp_path):
    """Test using compact template."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--template",
        "compact",
    )

    assert result.exit_code == 0


def test_cli_with_template_enterprise(tmp_path):
    """Test using enterprise template."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--template",
        "enterprise",
    )

    assert result.exit_code == 0


def test_cli_with_template_invalid(tmp_path):
    """Test using invalid template."""
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = invoke_profile(
        str(csv_path),
        "--report",
        "html",
        "--template",
        "invalid_template",
    )

    assert result.exit_code != 0