class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack <pair<int, int>> st;
        vector<int> d(size(temperatures), 0);
        for (int i = 0; i < size(temperatures); i++) {
            while (size(st) != 0) {
                pair<int, int> t = st.top();
                if (temperatures[i] > get<0>(t)) {
                    d[get<1>(t)] = i - get<1>(t);
                    st.pop();
                } else {
                    break;
                }
            }
            st.push(make_pair(temperatures[i], i));
        }
        return d;
    }
};
