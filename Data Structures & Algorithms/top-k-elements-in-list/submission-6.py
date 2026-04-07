class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        v = list(d.values())
        ke = list(d.keys())

        l = []
        for i in range(k):
            m = max(v)
            pos = v.index(m)          
            l.append(ke[pos])
            ke.pop(pos)
            v.pop(pos)
        return l
