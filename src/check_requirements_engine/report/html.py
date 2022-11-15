from typing import Any

from jinja2 import Environment, FileSystemLoader

from check_requirements_engine.models import RequirementData

ENVIRONMENT = Environment(loader=FileSystemLoader("check_requirements_engine/report/templates"))
ENVIRONMENT.trim_blocks = True
ENVIRONMENT.lstrip_blocks = True


def render_template(template_name: str, context: dict[Any, Any]):
    template = ENVIRONMENT.get_template(template_name)
    return template.render(context)


def html_report(requirements: dict[str, RequirementData]) -> str:
    output = render_template("report_template.html", {"requirements": requirements})
    return output
