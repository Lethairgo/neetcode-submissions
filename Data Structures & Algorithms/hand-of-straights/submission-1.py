class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand) # {card val: freq}
        minHeap = list(count.keys()) # [hand[1], ...., hand[i], ... hand[n - 1]]
        heapq.heapify(minHeap)

        while minHeap:
            minVal = minHeap[0]
            for val in range(minVal, minVal + groupSize):
                if val not in count:
                    return False
                count[val] -= 1
                if count[val] == 0:
                    heapq.heappop(minHeap)
        return True