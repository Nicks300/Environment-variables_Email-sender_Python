from typing import List, Union, Tuple, Optional


def number_of_differences(lst1: List[Union[int, str, bool]], lst2: List[Union[int, str, bool]]) -> int:
    count = 0
    correct = 0
    for item in lst2:
        if isinstance(item, str) or isinstance(item, int) or isinstance(item, bool):
            if item in lst1:
                count += 1
            correct += 1
    count = correct - count
    return count


def calculate_area(name: str, l: Tuple[float, ...]) -> Optional[float]:
    if name == 'rectangle' and isinstance(name, str) and len(l) == 2 and isinstance(l[0],
                                                                                    float) and isinstance(
        l[1], float) and isinstance(l, tuple):
        return round(l[0] * l[1], 2)
    elif name == 'circle' and isinstance(name, str) and len(l) == 1 and isinstance(l[0],
                                                                                   float) and isinstance(l, tuple):
        return round(3.14159 * l[0] * l[0], 2)
    else:
        return None


# def main():
#     name = "rectangle"
#     l = [1.0, 2.0]
#     print(calculate_area(name, l))
#     name = "circle"
#     l = (1.0,)
#     print(calculate_area(name, l))
#     print(number_of_differences([1, 2, 3.0, 4.0, 5.0, True], [True, "rt", 2.0, False, "wer", 1, 5.0]))
#     print(number_of_differences([1, 2, 3.0, 4.0, 5.0, 6, 7], [2, 6, 7]))
#
#
# if __name__ == '__main__':
#     main()
