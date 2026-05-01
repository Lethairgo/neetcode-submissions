class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0

        while start < n:
            end = start
            tank = 0
            count = 0

            while count < n:
                i = end % n
                tank += gas[i] - cost[i]

                if tank >= 0:
                    count += 1
                    end += 1
                else:
                    break

            if count == n:
                return start
            start = end + 1
        
        return -1

        