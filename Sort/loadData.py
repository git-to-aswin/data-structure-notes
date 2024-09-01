def loadList(filename='../data/sort.txt'):
    with open(filename, 'r') as file:
        data  = file.read().split("\n")
        return [[int(v) for v in d.split(",")] for d in data ]