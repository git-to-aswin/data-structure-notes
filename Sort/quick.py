def quickSort(v: list) -> list:
    if len(v) < 2:
        return v

    pivot = v[0]
    i, j = 1, len(v) - 1

    while i <= j:
        if v[i] > pivot and v[j] <= pivot:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
        if v[i] <= pivot:
            i += 1
        if v[j] > pivot:
            j -= 1

    # Place pivot in its correct position
    v[0], v[j] = v[j], v[0]

    # Recursively sort the partitions
    left = quickSort(v[:j])
    right = quickSort(v[j + 1:])

    return left + [v[j]] + right


if __name__ == "__main__":
    listV = [[34, 12, 654, 34, 21, 786, 43, 8, 67, 12, 96, 34]]
    for v in listV:
        print(f"Original: {v}")
        sorted_v = quickSort(v)
        print(f"Sorted: {sorted_v}")
