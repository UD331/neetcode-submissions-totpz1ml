class Solution {
public:
    int maxArea(vector<int>& heights) {
        int m = 0, l = 0, r = heights.size() - 1;
        while (l <r) {
            if (heights[l] < heights[r]) {
                m = max(m, heights[l] *(r-l));
                l++;
            }else{
                m = max(m, heights[r] *(r-l));
                r--;
            }
        }
        return m;
    }
};
