class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        l, m = 0, 0
        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            m = max(m, r-l+1)
        return m
            