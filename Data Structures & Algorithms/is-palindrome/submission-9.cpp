
class Solution {
public:
    bool isPalindrome(string s) {
        string f, b;
        for (char ch: s) {
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                //cout << tolower(ch) << "\n";
                f = f+ char(tolower(ch));
                b = char(tolower(ch)) + b;
            } else if ((ch >= '0' && ch <= '9')) {
                f = f+ char((ch));
                b = char((ch)) + b;
            }
        }
        cout << f << "\n";
        cout << b;
        return f == b;
    }
};
