class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        if nums:        
            c = 1
            m1 = min(nums)
            nums.pop(nums.index(m1))
            while nums:
                m2 = min(nums)
                nums.pop(nums.index(m2))
                if m2 == m1+1:
                    print(m1)
                    print(m2)
                    c += 1
                elif m1 != m2:
                    if c >= m:
                        m = c
                        c = 1
                m1 = m2
            if c > m:
                m = c
        return m    
