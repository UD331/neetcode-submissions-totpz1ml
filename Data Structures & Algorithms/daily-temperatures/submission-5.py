class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        temp = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i] > st[-1][0]:
                t, ind = st.pop()
                temp[ind] = i-ind
            st.append((temperatures[i], i))
        return temp

