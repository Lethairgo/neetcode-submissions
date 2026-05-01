class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # no overlapping
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else: # overlapping
                temp = []
                temp.append(min(intervals[i][0], newInterval[0]))
                temp.append(max(intervals[i][1], newInterval[1]))
                newInterval = temp
        result.append(newInterval)
        return result