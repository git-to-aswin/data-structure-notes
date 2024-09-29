def mergeSort(v):
    if len(v) <= 1:
        return v

    mid = len(v) // 2
    s1 = mergeSort(v[:mid])
    s2 = mergeSort(v[mid:])
    
    return merge(s1, s2)

def merge(s1, s2):
    i, j = 0, 0
    s3 = []
    
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            s3.append(s1[i])
            i += 1
        else:
            s3.append(s2[j])
            j += 1
    
    # Add remaining elements
    s3.extend(s1[i:])
    s3.extend(s2[j:])
    
    return s3

if __name__ == "__main__":
    listV = [[12,654,34,21,786,43,8,67,12,96,467,34]]
    for v in listV:
        print(f"Original: {v}")
        sorted_v = mergeSort(v)
        print(f"Sorted: {sorted_v}")