from loadData import loadList
'''
    Brute force
    for best n worst case - O(n^2)
    - iterate thorugh each element and find the minimum and put it in front
'''
def selectionSort(v:list):
    for pointer in range(0,len(v)):
        smallVal = float("inf")
        smallIdx = None
        for idx in range(pointer,len(v)):
            if v[idx] < smallVal:
                smallIdx , smallVal= idx, v[idx]
        else:
            v[smallIdx], v[pointer] = v[pointer], v[smallIdx]
        
if __name__ == "__main__":
    listV = loadList()
    for v in listV:
        print(v)
        selectionSort(v)
        print(v)