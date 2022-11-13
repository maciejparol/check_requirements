import requests
import requirements


from src.check_requirements.models import RequirementData


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
