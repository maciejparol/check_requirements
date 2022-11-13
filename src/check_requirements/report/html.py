from typing import Any

from jinja2 import Environment, FileSystemLoader

from src.check_requirements.models import RequirementData

ENVIRONMENT = Environment(loader=FileSystemLoader("report/templates"))
ENVIRONMENT.trim_blocks = True
ENVIRONMENT.lstrip_blocks = True


def render_template(template_name: str, context: dict[Any, Any]):
    template = ENVIRONMENT.get_template(template_name)
    return template.render(context)


def html_report(requirements: dict[str, RequirementData]) -> str:
    output = render_template("report_template.html", {"requirements": requirements})
    return output
