from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from aniwa.models.profile import DatasetProfile


PDF_THEMES = {
    "default": {
        "page_bg": "#f8fafc",
        "text": "#0f172a",
        "muted": "#64748b",
        "summary": "#2563eb",
        "schema": "#0f172a",
        "statistics": "#7c3aed",
        "insights": "#ca8a04",
        "body_bg": "#ffffff",
        "row_alt": "#f8fafc",
        "grid": "#e2e8f0",
    },
    "clean": {
        "page_bg": "#ffffff",
        "text": "#111827",
        "muted": "#6b7280",
        "summary": "#111827",
        "schema": "#374151",
        "statistics": "#4b5563",
        "insights": "#6b7280",
        "body_bg": "#ffffff",
        "row_alt": "#f9fafb",
        "grid": "#e5e7eb",
    },
    "compact": {
        "page_bg": "#ffffff",
        "text": "#111827",
        "muted": "#6b7280",
        "summary": "#334155",
        "schema": "#1f2937",
        "statistics": "#475569",
        "insights": "#64748b",
        "body_bg": "#ffffff",
        "row_alt": "#f8fafc",
        "grid": "#e5e7eb",
    },
    "enterprise": {
        "page_bg": "#eff6ff",
        "text": "#172554",
        "muted": "#475569",
        "summary": "#1d4ed8",
        "schema": "#1e3a8a",
        "statistics": "#0f766e",
        "insights": "#92400e",
        "body_bg": "#ffffff",
        "row_alt": "#eff6ff",
        "grid": "#bfdbfe",
    },
    "dark": {
        "page_bg": "#020617",
        "text": "#e5e7eb",
        "muted": "#94a3b8",
        "summary": "#0f172a",
        "schema": "#1e293b",
        "statistics": "#334155",
        "insights": "#0369a1",
        "body_bg": "#0f172a",
        "row_alt": "#111827",
        "grid": "#334155",
    },
}


def render_pdf_report(
    profile: DatasetProfile,
    output: str,
    template: str = "default",
) -> None:
    theme = _get_theme(template)
    output_path = Path(output)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=landscape(letter),
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()
    styles["Title"].textColor = colors.HexColor(theme["text"])
    styles["Heading2"].textColor = colors.HexColor(theme["text"])
    styles["BodyText"].textColor = colors.HexColor(theme["muted"])
    styles["Italic"].textColor = colors.HexColor(theme["muted"])

    elements = []

    elements.append(Paragraph("Aniwa Dataset Profile", styles["Title"]))
    elements.append(
        Paragraph(
            "Universal dataset profiling and intelligence report.",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Dataset Summary", styles["Heading2"]))

    summary_data = [
        ["Metric", "Value"],
        ["Rows", f"{profile.summary.rows:,}"],
        ["Columns", f"{profile.summary.columns:,}"],
        ["Duplicate Rows", f"{profile.quality.duplicate_rows:,}"],
        ["Duplicate %", f"{profile.quality.duplicate_percent}%"],
    ]

    summary_table = Table(summary_data, colWidths=[200, 200])
    _style_table(summary_table, header_color=theme["summary"], theme=theme)
    elements.append(summary_table)
    elements.append(Spacer(1, 24))

    elements.append(Paragraph("Schema Profile", styles["Heading2"]))

    column_data = [["Column", "Type", "Nulls", "Null %", "Unique"]]

    for col in profile.columns:
        column_data.append(
            [
                col.name,
                col.dtype,
                f"{col.null_count:,}",
                f"{col.null_percent}%",
                f"{col.unique_count:,}",
            ]
        )

    column_table = Table(column_data, repeatRows=1)
    _style_table(column_table, header_color=theme["schema"], theme=theme)
    elements.append(column_table)
    elements.append(Spacer(1, 24))

    numeric_columns = [col for col in profile.columns if col.numeric_stats]

    if numeric_columns:
        elements.append(Paragraph("Numeric Statistics", styles["Heading2"]))

        stats_data = [["Column", "Min", "Max", "Mean", "Median", "Std"]]

        for col in numeric_columns:
            stats = col.numeric_stats
            stats_data.append(
                [
                    col.name,
                    _format_value(stats.min),
                    _format_value(stats.max),
                    _format_value(stats.mean),
                    _format_value(stats.median),
                    _format_value(stats.std),
                ]
            )

        stats_table = Table(stats_data, repeatRows=1)
        _style_table(stats_table, header_color=theme["statistics"], theme=theme)
        elements.append(stats_table)
        elements.append(Spacer(1, 24))

    if profile.insights:
        elements.append(Paragraph("Insights", styles["Heading2"]))

        insight_data = [["Level", "Message"]]

        for insight in profile.insights:
            insight_data.append([insight.level.upper(), insight.message])

        insight_table = Table(insight_data, colWidths=[120, 620], repeatRows=1)
        _style_table(insight_table, header_color=theme["insights"], theme=theme)
        elements.append(insight_table)

    elements.append(Spacer(1, 24))
    elements.append(
        Paragraph(
            "Generated by Aniwa - See your data clearly.",
            styles["Italic"],
        )
    )

    doc.build(
        elements,
        onFirstPage=lambda canvas, doc: _draw_page_background(canvas, doc, theme),
        onLaterPages=lambda canvas, doc: _draw_page_background(canvas, doc, theme),
    )


def _get_theme(template: str) -> dict[str, str]:
    theme = PDF_THEMES.get(template)

    if theme is None:
        valid_templates = ", ".join(PDF_THEMES)
        raise ValueError(
            f"Invalid PDF report template: {template}. "
            f"Valid templates are: {valid_templates}."
        )

    return theme


def _draw_page_background(canvas, doc, theme: dict[str, str]) -> None:
    canvas.saveState()
    canvas.setFillColor(colors.HexColor(theme["page_bg"]))
    canvas.rect(
        0,
        0,
        doc.pagesize[0],
        doc.pagesize[1],
        fill=1,
        stroke=0,
    )
    canvas.restoreState()


def _style_table(
    table: Table,
    header_color: str,
    theme: dict[str, str],
) -> None:
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_color)),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor(theme["grid"])),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.HexColor(theme["body_bg"]),
                        colors.HexColor(theme["row_alt"]),
                    ],
                ),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor(theme["text"])),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
            ]
        )
    )


def _format_value(value: float | None) -> str:
    if value is None:
        return "-"

    if float(value).is_integer():
        return f"{int(value):,}"

    return f"{value:,.4f}"