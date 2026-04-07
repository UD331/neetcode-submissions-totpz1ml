class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mp = 0;
        int n = prices[0];
        for (int i:prices) {
            mp = max(mp, i-n);

            n = min(i,n);
        }
        return mp;
    }
};
