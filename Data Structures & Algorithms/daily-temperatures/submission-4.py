class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n
        for i in range(n):
            while st and temperatures[i] > st[-1][0]:
                te, j = st.pop()
                res[j] = i-j;
            st.append((temperatures[i], i))

        return res


