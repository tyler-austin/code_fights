def extract_each_kth(input_array: list, k: int):
    result = []
    for i, e in enumerate(input_array):
        if (i + 1) % k != 0:
            result.append(e)
    return result
