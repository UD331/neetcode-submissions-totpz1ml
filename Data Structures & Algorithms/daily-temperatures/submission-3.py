class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n
        for i in range(n):
            while(st):
                temp, j = st.pop()
                if temp < temperatures[i]:
                    res[j] = i-j
                else:
                    st.append((temp, j))
                    break
            st.append((temperatures[i], i))
        return res


