class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i in range(len(digits)):
            s = s*10+digits[i]
        s+=1
        st = str(s)
        l = list(st)
        f = []
        for i in l:
            f.append(int(i))

        return f 