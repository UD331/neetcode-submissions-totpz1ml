class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        res = [intervals[0]]
        for s, e in intervals:
            end = res[-1][1]
            if s <= end:
                res[-1][1] = max(end, e)
            else:
                res.append([s,e])
        return res
            
            
