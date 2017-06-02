def is_lucky(num: int):
    digit_list = [int(d) for d in str(num)]
    i = len(digit_list) // 2
    first, second = 0, 0
    for d in digit_list[:i]:
        first += d
    for d in digit_list[i:]:
        second += d
    return first == second


if __name__ == '__main__':

    n = 1230

    print(is_lucky(n))
