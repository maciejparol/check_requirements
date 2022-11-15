import dataclasses
import json

from check_requirements_engine.models import RequirementData


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def json_report(requirements: dict[str, RequirementData]) -> str:
    return json.dumps(requirements, cls=EnhancedJSONEncoder)
