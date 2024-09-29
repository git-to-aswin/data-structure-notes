class Heap:
    def __init__(self) -> None:
        self.maxHeap = []

    def ins_heapify(self, idx):
        parentIdx = (idx - 1) // 2
        if idx > 0 and self.maxHeap[idx] > self.maxHeap[parentIdx]:
            # Swap child with parent if the child is greater
            self.maxHeap[parentIdx], self.maxHeap[idx] = self.maxHeap[idx], self.maxHeap[parentIdx]
            # Recursively heapify the parent
            self.ins_heapify(parentIdx)

    def insertHeap(self, data):
        # Append data to the heap list
        self.maxHeap.append(data)
        # Heapify from the newly added element to maintain heap property
        idx = len(self.maxHeap) - 1
        self.ins_heapify(idx)

    def del_heapify(self, idx):
        heapSize = len(self.maxHeap)
        lnode = 2 * idx + 1
        rnode = lnode + 1
        largest = idx

        # Check if left child exists and is greater than the current largest
        if lnode < heapSize and self.maxHeap[lnode] > self.maxHeap[largest]:
            largest = lnode

        # Check if right child exists and is greater than the current largest
        if rnode < heapSize and self.maxHeap[rnode] > self.maxHeap[largest]:
            largest = rnode

        # If the largest is not the root, swap and continue heapifying
        if largest != idx:
            self.maxHeap[idx], self.maxHeap[largest] = self.maxHeap[largest], self.maxHeap[idx]
            self.del_heapify(largest)

    def deleteHeap(self, data):
        try:
            idx = self.maxHeap.index(data)
        except ValueError:
            return "Not Found"

        heapSize = len(self.maxHeap)
        if heapSize == 0:
            return "Heap is empty"

        # Swap the element to delete with the last element
        self.maxHeap[idx], self.maxHeap[heapSize - 1] = self.maxHeap[heapSize - 1], self.maxHeap[idx]
        # Remove the last element
        self.maxHeap.pop()

        # Heapify from the swapped index
        self.del_heapify(idx)

    def getMax(self):
        if len(self.maxHeap) > 0:
            return self.maxHeap[0]
        return "Heap is empty"

    def printHeap(self):
        print(self.maxHeap)


if __name__ == "__main__":
    listV = [12, 654, 34, 21, 786, 43, 8, 67, 12, 96, 467, 34]
    heap = Heap()
    print(f"Original: {listV}")
    for v in listV:
        heap.insertHeap(v)

    print(f"Max Heap: {heap.maxHeap}")

    # Example of deleting an element
    heap.deleteHeap(786)
    print(f"Max Heap after deleting 786: {heap.maxHeap}")

    # Print the max element
    print(f"Current Max Element: {heap.getMax()}")
