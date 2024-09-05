from loadData import loadList
'''
    Brute force
    stable sort
    for best n worst case - O(n^2)
    - check with adjacent and do it continusly until n times
'''
def bubbleSort(v:list):
    for _ in range(0,len(v)):
        for j in range(0,len(v)-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
        
if __name__ == "__main__":
    listV = loadList()
    for v in listV:
        print(v)
        bubbleSort(v)
        print(v)