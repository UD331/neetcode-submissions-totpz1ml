class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        mf, l, c = 0,0,0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r],0)+1
            mf = max(mf, dic[s[r]])
            while r-l+1-k>mf:
                dic[s[l]]-=1
                l+=1
            c = max(c, r-l+1)
        return c
