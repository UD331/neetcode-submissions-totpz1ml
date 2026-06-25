class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s)-1
        l = 0
        while l < r:
            t = s[r]
            s[r] = s[l]
            s[l] = t
            r-=1
            l+=1
        