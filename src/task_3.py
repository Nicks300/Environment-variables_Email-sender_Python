from typing import Dict, List, Any


def comparison_dict_and_list(dictionary: Dict[str, str], string_list: List[str]) -> bool:
    for elem in string_list:
        if elem in dictionary.values():
            return True
    return False


def get_user_info(user_list: List[Dict[str, Any]], user_name: str) -> Dict[str, Any] | None:
    for user in user_list:
        if user['name'] == user_name:
            return user
    return None
