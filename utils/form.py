
def is_field_required_provided(data: dict, REQUIRED_FIELDS: list[str]) -> set[bool, str]:

    for f_name in REQUIRED_FIELDS:
        f_value = data.get(f_name, 'None')

        if f_value is None:
            return False, f_name

    return True, "pass"