import requests
import requirements

from src.check_requirements.models import RequirementData
from src.check_requirements.report.console import console_report
from src.check_requirements.report.html import html_report
from src.check_requirements.report.json import json_report

req_files = [
    "/home/maciej/PycharmProjects/check_requirements/req.txt",
    # "/home/maciej/PycharmProjects/check_requirements/req2.txt",
]


def _set_requirement_data() -> dict:
    pass


def check_requirements_in_file(file_name: str) -> dict:
    tmp_data = {}
    with open(file_name, "r") as fd:
        for req in requirements.parse(fd):
            if not req.line.startswith("git+"):
                request = requests.get(f"https://pypi.org/pypi/{req.name}/json")
                current_version = req.specs[0][1]
                if request.ok:
                    request_json = request.json()
                    tmp_data[req.name] = RequirementData(
                        current_version=current_version,
                        latest_version=request_json["info"]["version"],
                        vulnerabilities=request_json["vulnerabilities"],
                        found_in_pypi=True,
                    )
                else:
                    tmp_data[req.name] = RequirementData(
                        current_version=current_version,
                        latest_version="-",
                        vulnerabilities=[],
                        found_in_pypi=False,
                    )

    return tmp_data


def check(files: list[str], output=console_report):
    tmp_ = {}
    for file in files:
        tmp_[file] = check_requirements_in_file(file)
    print(output(tmp_))


if __name__ == "__main__":
    check(req_files)
