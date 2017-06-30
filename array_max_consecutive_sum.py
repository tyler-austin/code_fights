def array_max_consecutive_sum(a: list, k: int):
    sums = list()
    rs = sum(a[:k])
    sums.append(rs)
    for i in range(1, len(a[:-(k-1)]), 1):
        rs += a[i+(k-1)] - a[i-1]
        sums.append(rs)
    return max(sums)
