class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        temp = [0]*len(temperatures)
        for i in range(len(temperatures)):
            tem = temperatures[i]
            while st and  tem > st[-1][0]:
                t, ind = st.pop()
                temp[ind] = i-ind
            st.append((tem, i))
        return temp

