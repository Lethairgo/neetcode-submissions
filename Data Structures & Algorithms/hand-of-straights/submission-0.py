class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand) # {card val: freq}

        for val in sorted(count): # sort by the key of count, which is card val
            freq = count[val]
            if freq > 0:
                for num in range(val, val + groupSize):
                    if count[num] < freq:
                        return False
                    count[num] -= freq

        return True