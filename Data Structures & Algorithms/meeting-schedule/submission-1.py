"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: 
            return True
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0].start
        for interval in intervals:
            if interval.start < prev:
                return False
            prev = interval.end
        return True