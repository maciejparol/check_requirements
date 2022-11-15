from dataclasses import dataclass, field
from typing import List


@dataclass
class RequirementData:
    current_version: str
    latest_version: str
    vulnerabilities: List = field(default_factory=lambda: [])
    found_in_pypi: bool = field(default=False)

    @property
    def equal_versions(self) -> bool:
        return self.current_version == self.latest_version

    @property
    def human_found_in_pypi(self) -> str:
        return str(self.found_in_pypi)

    @property
    def vulnerabilities_list(self) -> str:
        return ", ".join(self.vulnerabilities)
