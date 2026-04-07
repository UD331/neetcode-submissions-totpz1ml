class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                temp = st.pop()
                if c == ')' and temp != '(':
                    return False
                elif c == '}' and temp != '{':
                    return False
                elif c == ']' and temp != '[':
                    return False
            
        if len(st) != 0:
            return False    
        return True