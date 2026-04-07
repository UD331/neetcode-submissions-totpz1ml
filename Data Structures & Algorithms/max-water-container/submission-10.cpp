class Solution {
public:
    int maxArea(vector<int>& heights) {
        int m = 0, l = 0, r = heights.size() - 1;
        while (l <r) {
            int mi = min(heights[l], heights[r]);
            m = max(m, mi*(r-l));
            if (mi == heights[l])
                l++;
            else
                r--;
        }
        return m;
    }
};
