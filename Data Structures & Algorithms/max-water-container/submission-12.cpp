class Solution {
public:
    int maxArea(vector<int>& heights) {
        int m = 0, l = 0, r = heights.size() - 1;
        while (l < r) {
            int lh = heights[l], rh = heights[r];
            if (lh < rh) {
                m = max(m, (r-l)*lh);
                l++;
            } else {
                m = max(m, (r-l)*rh);
                r--;
            }
        }
        return m;
    }
};
