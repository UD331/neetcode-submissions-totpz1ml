class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        st = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if (len(st) == 0):
                    return False
                t = st.pop()
                if i == ")" and t != "(":
                    return False
                if i == "}" and t != "{":
                    return False
                if i == "]" and t != "[":
                    return False
        if (len(st) == 0):
            return True
        else:
            return False