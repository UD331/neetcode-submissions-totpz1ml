class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        no = set()
        for n in nums:
            if n in no:
                return n
            no.add(n)
            