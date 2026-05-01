class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        bench = int(len(nums)/3)
        res = set()
        dic = {}
        for n in nums:
            c = dic.get(n, 0)+1
            dic[n] = c
            if c>bench:
                res.add(n)
        return list(res)