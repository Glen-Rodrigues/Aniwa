import platform
import time
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

import typer

from aniwa import __version__
from aniwa.core.profiler import profile_dataframe
from aniwa.io.readers import read_dataset
from aniwa.models.enums import ReportSection
from aniwa.models.profile import ProfileMetadata
from aniwa.reports.console import render_console_report
from aniwa.reports.excel_report import render_excel_report
from aniwa.reports.html_report import render_html_report
from aniwa.reports.json_report import render_json_report
from aniwa.reports.markdown_report import render_markdown_report
from aniwa.reports.pdf_report import render_pdf_report


app = typer.Typer(help="Aniwa - Universal dataset profiling and intelligence.")


class ReportFormat(str, Enum):
    console = "console"
    json = "json"
    html = "html"
    excel = "excel"
    markdown = "markdown"
    pdf = "pdf"


class ProfileMode(str, Enum):
    fast = "fast"
    deep = "deep"


def validate_sections(value: str | None) -> list[str] | None:
    if not value:
        return None

    split_sections = [item.strip() for item in value.split(",")]
    valid_options = [section.value for section in ReportSection]

    for section in split_sections:
        if section not in valid_options:
            raise typer.BadParameter(
                f"Invalid report section: {section}. "
                f"Valid options are: {', '.join(valid_options)}."
            )

    return split_sections


def resolve_sections(
    include: str | None,
    exclude: str | None,
) -> set[ReportSection]:
    include_sections = validate_sections(include)
    exclude_sections = validate_sections(exclude)

    if include_sections and exclude_sections:
        raise typer.BadParameter("Use either --include or --exclude, not both.")

    all_sections = set(ReportSection)

    if include_sections:
        return {ReportSection(section) for section in include_sections}

    if exclude_sections:
        return all_sections - {ReportSection(section) for section in exclude_sections}

    return all_sections


def format_file_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    if size_bytes < 1024**2:
        return f"{size_bytes / 1024:.2f} KB"

    if size_bytes < 1024**3:
        return f"{size_bytes / 1024**2:.2f} MB"

    return f"{size_bytes / 1024**3:.2f} GB"


def build_profile_metadata(
    dataset_path: Path,
    mode: ProfileMode,
    report: ReportFormat,
    template: str,
    sections: set[ReportSection],
    include: str | None,
    exclude: str | None,
    duration_seconds: float,
) -> ProfileMetadata:
    include_sections = validate_sections(include)
    exclude_sections = validate_sections(exclude)

    return ProfileMetadata(
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        aniwa_version=__version__,
        python_version=platform.python_version(),
        dataset_path=str(dataset_path),
        dataset_file_type=dataset_path.suffix.lower().lstrip(".").upper(),
        dataset_size=format_file_size(dataset_path.stat().st_size),
        profiling_mode=mode.value,
        report_format=report.value,
        report_template=template if report in {ReportFormat.html, ReportFormat.pdf} else None,
        included_sections=include_sections or sorted(section.value for section in sections),
        excluded_sections=exclude_sections,
        profiling_duration=f"{duration_seconds:.2f}s",
    )


@app.command()
def profile(
    path: str = typer.Argument(..., help="Path to dataset file."),
    report: ReportFormat = typer.Option(
        ReportFormat.console,
        "--report",
        "-r",
        help="Report format.",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path.",
    ),
    mode: ProfileMode = typer.Option(
        ProfileMode.deep,
        "--mode",
        "-m",
        help="Profiling mode. Use 'fast' for lightweight checks or 'deep' for full profiling.",
    ),
    include: str | None = typer.Option(
        None,
        "--include",
        "-i",
        help="Comma-separated list of report sections to include.",
    ),
    exclude: str | None = typer.Option(
        None,
        "--exclude",
        "-e",
        help="Comma-separated list of report sections to exclude.",
    ),
    template: str = typer.Option(
        "default",
        "--template",
        "-t",
        help="Report template for HTML/PDF outputs. Options: default, clean, compact, enterprise, dark.",
    ),
):
    """
    Profile a dataset.
    """
    sections = resolve_sections(include, exclude)

    dataset_path = Path(path)

    if not dataset_path.exists():
        raise typer.BadParameter(f"File does not exist: {path}")

    start_time = time.perf_counter()

    df = read_dataset(path)
    dataset_profile = profile_dataframe(df, mode=mode.value, sections=sections)

    duration_seconds = time.perf_counter() - start_time

    dataset_profile.metadata = build_profile_metadata(
        dataset_path=dataset_path,
        mode=mode,
        report=report,
        template=template,
        sections=sections,
        include=include,
        exclude=exclude,
        duration_seconds=duration_seconds,
    )

    if report == ReportFormat.console:
        render_console_report(dataset_profile)
        return

    if report == ReportFormat.json:
        json_output = render_json_report(dataset_profile, output)

        if output:
            typer.echo(f"JSON report written to {output}")
        else:
            typer.echo(json_output)

        return

    if report == ReportFormat.html:
        if output is None:
            output = "aniwa_report.html"

        try:
            render_html_report(dataset_profile, output, template=template)
        except ValueError as exc:
            raise typer.BadParameter(str(exc)) from exc

        typer.echo(f"HTML report written to {output}")
        return

    if report == ReportFormat.excel:
        if output is None:
            output = "aniwa_report.xlsx"

        try:
            render_excel_report(dataset_profile, output)
        except ValueError as exc:
            raise typer.BadParameter(str(exc)) from exc

        typer.echo(f"Excel report written to {output}")
        return

    if report == ReportFormat.markdown:
        markdown_output = render_markdown_report(dataset_profile, output)

        if output:
            typer.echo(f"Markdown report written to {output}")
        else:
            typer.echo(markdown_output)

        return

    if report == ReportFormat.pdf:
        if output is None:
            output = "aniwa_report.pdf"

        try:
            render_pdf_report(dataset_profile, output, template=template)
        except ValueError as exc:
            raise typer.BadParameter(str(exc)) from exc

        typer.echo(f"PDF report written to {output}")
        return