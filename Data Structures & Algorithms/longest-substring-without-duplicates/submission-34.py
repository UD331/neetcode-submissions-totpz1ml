class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            res = max(res, r-l+1)
        return res
            