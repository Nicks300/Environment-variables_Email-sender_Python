from typing import Tuple, List, Dict


def process_numbers(numbers: List[int]) -> Tuple[int, int, int]:
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = round(sum(numbers) / len(numbers), 1)
    return min_num, max_num, avg_num


def find_item(dictionary: Dict, key: str) -> int | None:
    if key in dictionary:
        return dictionary[key]
    else:
        return None
