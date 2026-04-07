"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        if not intervals:
            print(intervals)
            return True
        out = intervals[0]
        for i in range(1, len(intervals)):
            s = intervals[i]
            if s.start in range(out.start, out.end):
                return False
            out = intervals[i]
        return True