class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ['+', '-', '*', '/']
        for i in tokens:
            if i not in op:
                    st.append(i)
            else:
                    if i == '+':
                        st.append(int(st.pop()) + int(st.pop()))
                    elif i == '-':
                        st.append(int(st.pop(-2)) - int(st.pop(-1)))
                    elif i == '*':
                        st.append(int(st.pop()) * int(st.pop()))
                    elif i == '/':
                        st.append(int(int(st.pop(-2)) / int(st.pop(-1))))
        return int(st.pop())
