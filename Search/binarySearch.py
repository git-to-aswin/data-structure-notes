def binarySearch(S:list, val):
    l = int(len(S)/2)
    print(S,l)
    if S[l] > val:
        binarySearch(S[:l],val)
    elif S[l] < val:
        binarySearch(S[l:],val)
    else:
        if S[l] == val:
            print(val)
        else:
            print("Not found")
        
    

if __name__ == "__main__":
    S = [1,3,5,7,8,9,10,23,45,67,89,156,258,479]
    val = 23
    binarySearch(S, val)