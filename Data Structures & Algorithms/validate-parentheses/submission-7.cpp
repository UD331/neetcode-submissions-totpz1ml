class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c: s) {
            if (c == '{' || c == '(' || c == '[')
                st.push(c);
            else {
                if (st.empty())
                    return false;
                char p = st.top();
                st.pop();
                if (p == '{' && c != '}')
                    return false;
                if (p == '(' && c != ')')
                    return false;
                if (p == '[' && c != ']')
                    return false;
            }
        }
        
        return st.empty();
    }
};
