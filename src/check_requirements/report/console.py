from src.check_requirements.models import RequirementData

HEADER = "\033[95m| {:<30} | {:<20} | {:<20} | {:<20} | {:20}\033[0m\n".format(
    "Package Name", "Current Version", "Latest Version", "Vulnerabilities", "In PYPI"
)
HEADER_LEN = len(HEADER)


def console_report(requirements: dict[str, RequirementData]) -> str:
    print_data = ""
    for file_name, requirement in requirements.items():

        p = int((HEADER_LEN - len(file_name) - 13) / 2)
        print_data += "\n\n{0} FILE NAME: \033[91m{1}\033[0m {2}\n".format(
            "=" * p, file_name, "=" * p
        )

        print_data += HEADER
        print_data += "\033[95m-\033[0m" * HEADER_LEN
        for name, requirement_item in requirement.items():
            print_format = "\n\033[95m| {:<30}\033[0m "
            if requirement_item.equal_versions:
                print_format = print_format + "|\033[92m {:<20}\033[0m | {:<20} "
            else:
                print_format = (
                    print_format + "| \033[91m{:<20}\033[0m |\033[92m {:<20}\033[0m "
                )
            print_format = print_format + "| {:<20} "
            if requirement_item.found_in_pypi:
                print_format = print_format + "| \033[92m{:<20}\033[0m "
            else:
                print_format = print_format + "| \033[91m{:<20}\033[0m "
            print_data += print_format.format(
                name,
                requirement_item.current_version,
                requirement_item.latest_version,
                requirement_item.vulnerabilities_list,
                requirement_item.human_found_in_pypi,
            )
    return print_data
