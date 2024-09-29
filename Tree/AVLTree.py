class Node:
    def __init__(self, data) -> None:
        self.left: 'Node' = None
        self.right: 'Node' = None
        self.value = data
        self.height = 1

    def updateHeight(self):
        self.height = max(self.left.height if self.left else 0, self.right.height if self.right else 0) + 1

    def balanceFactor(self):
        return (self.left.height if self.left else 0) - (self.right.height if self.right else 0)
    
    def rotateLeft(self):
        newNode = self.right
        self.right = newNode.left
        newNode.left = self
        
        self.updateHeight()
        newNode.updateHeight()

        return newNode
    
    def rotateRight(self):
        newNode = self.left
        self.left = newNode.right
        newNode.right = self

        self.updateHeight()
        newNode.updateHeight()

        return newNode

    def balanceTree(self, balanceFactor, data):
        # Left-Left (LL) Case - Right rotation needed
        if balanceFactor > 1 and data < self.left.value:
            return self.rotateRight()

        # Right-Right (RR) Case - Left rotation needed
        if balanceFactor < -1 and data > self.right.value:
            return self.rotateLeft()

        # Left-Right (LR) Case - Left rotation on left child, then right rotation
        if balanceFactor > 1 and data > self.left.value:
            self.left = self.left.rotateLeft()
            return self.rotateRight()

        # Right-Left (RL) Case - Right rotation on right child, then left rotation
        if balanceFactor < -1 and data < self.right.value:
            self.right = self.right.rotateRight()
            return self.rotateLeft()

        return self

    def checkMininumRight(self):
        leastNode = self
        while leastNode.left:
            leastNode = leastNode.left
        return leastNode
    
    def checkMaximumLeft(self):
        maxNode = self
        while maxNode.right:
            maxNode = maxNode.right
        return maxNode

    def insert(self, data):
        if data < self.value:
            if self.left:
                self.left = self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.value:
            if self.right:
                self.right = self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            return self

        self.updateHeight()

        return self.balanceTree(self.balanceFactor(), data)

    def delete(self, data):
        if data < self.value:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.value:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                if self.left.height > self.right.height:
                    exchangeNode = self.checkMaximumLeft()
                    self.value = exchangeNode.value
                    self.left = self.left.delete(exchangeNode.value)
                else:
                    exchangeNode = self.checkMininumRight()
                    self.value = exchangeNode.value
                    self.right = self.right.delete(exchangeNode.value)

        self.updateHeight()

        return self.balanceTree(self.balanceFactor(), data)

    def preOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

if __name__ == "__main__":
    listV = [12, 654, 34, 21, 786, 43, 8, 67, 12, 96, 467, 34]

    print(f"Original: {listV}")
    node = Node(10)

    for v in listV:
        node = node.insert(v)

    print("Pre-order traversal of the AVL tree:")
    node.preOrder()
    print()  # For better output formatting
