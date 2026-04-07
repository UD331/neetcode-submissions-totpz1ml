class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        b = False
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    st.append(j-i)
                    b = True
                    break
            if not b:
                st.append(0)
            b = False
        return st

            