def process_numbers(numbers: list[int]) -> tuple:
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = round(sum(numbers) / len(numbers), 1)
    return min_num, max_num, avg_num

def find_item(dictionary: dict[str:int], key: str) -> int|None:
    if key in dictionary:
        return dictionary[key]
    else:
        return None
