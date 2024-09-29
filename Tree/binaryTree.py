
class Node:
    def __init__(self, l:list) -> None:
        self.data = None
        self.lnode : 'Node' = None
        self.rnode : 'Node' = None
    
    def insert(self,val):
        if self.data == None:
            self.data = val
        elif val <= self.data:
            if self.lnode is None:
                self.lnode = Node()
            self.lnode.insert(val)
        else:
            if self.rnode is None:
                self.rnode = Node()
            self.rnode.insert(val)

def binaryTree(l):
    node = Node()
    for val in l:
        node.insert(val)


if __name__ == "__main__":
    listV = [[12,654,34,21,786,43,8,67,12,96,467,34]]
    for v in listV:
        print(f"Original: {v}")
        sorted_v = binaryTree(v)
        print(f"Sorted: {sorted_v}")