from typing import Any, Dict


def is_subdict(super_dict: Dict[str, Any], sub_dict: Dict[str, Any]) -> bool:
    """
    If all the keys in the sub_dict are in the super_dict and have the same values, then return True.

    :param super_dict: The dictionary that you want to check if it contains the sub_dict
    :type super_dict: Dict[str, Any]
    :param sub_dict: The dictionary that you want to check if it's a subset of super_dict
    :type sub_dict: Dict[str, Any]
    :return: A list of dictionaries
    """
    found_list = []
    for key, val in sub_dict.items():
        super_val = super_dict.get(key, None)
        if isinstance(val, str) and isinstance(super_val, str):
            condition = super_val.strip().lower() == val.strip().lower()
        else:
            condition = super_val == val

        found_list.append(condition)

    return all(found_list)
