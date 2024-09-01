from loadData import loadList
'''
    Decrease and conquer
    for worst case - O(n^2)
    - iterate through the array with one pointer which act as a pivot pointer
    - The point before the pivot pointer should be sorted each time
'''
def insertionSort(v:list):
    for pointer in range(0,len(v)):
        temp = None
        for tempPtr in range(0,pointer+1):
            if temp != None:
                v[tempPtr], temp = temp , v[tempPtr]
            elif v[tempPtr] > v[pointer]:
                temp, v[tempPtr] = v[tempPtr], v[pointer]

if __name__ == "__main__":
    listV = loadList()
    for v in listV:
        print(v)
        insertionSort(v)
        print(v)