from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from aniwa.models.profile import DatasetProfile


def render_html_report(profile: DatasetProfile, output: str | None = None) -> str:
    template_dir = Path(__file__).parent / "templates"

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("report.html")

    html = template.render(profile=profile)

    if output:
        Path(output).write_text(html, encoding="utf-8")

    return html