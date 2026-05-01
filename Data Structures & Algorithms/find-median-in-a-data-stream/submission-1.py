class MedianFinder:

    def __init__(self):
        self.minHeap = [] # large half
        self.maxHeap = [] # small half
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -temp)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        