import os
from typing import Callable

import click

from click import Option, Context

from check_requirements_engine._check import check_requirements_in_file
from check_requirements_engine.report.console import console_report
from check_requirements_engine.report.html import html_report
from check_requirements_engine.report.json import json_report
import logging


REPORT_TYPES = ["console", "html", "json"]


def validate_report(ctx: Context, param: Option, value: str) -> Callable:
    if value in REPORT_TYPES:
        if value == "console":
            return console_report
        elif value == "html":
            return html_report
        elif value == "json":
            return json_report
    else:
        raise click.BadParameter(f"Possible options: {', '.join(REPORT_TYPES)}")


def validate_files(ctx: Context, param: Option, value: list[str]) -> Callable:
    list_files = []
    for path in value:
        if os.path.isfile(path):
            list_files.append(path)
        else:
            logging.warning(f"Not found file: {path} - omitted")
    if len(list_files) < 1:
        logging.warning("Omitted all files")
    return list_files


@click.command()
@click.option(
    "--files", "-f", multiple=True, callback=validate_files
)
@click.option(
    "--report",
    "-r",
    default="console",
    help=f"Report type: {', '.join(REPORT_TYPES)}. Default - console",
    callback=validate_report,
)
def check_requirements(files: list[str], report):

    tmp_ = {}
    for file in files:
        tmp_[file] = check_requirements_in_file(file)
    print(report(tmp_))



if __name__ == "__main__":
    check_requirements()
