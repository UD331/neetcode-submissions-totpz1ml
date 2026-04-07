class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        for i in range(len(temperatures)):
            c = 0
            for j in range(i+1, (len(temperatures))):
                if temperatures[j] > temperatures[i]:
                    st.append(j-i)
                    c = 1
                    break
            if c == 0:
                st.append(0)
        return st