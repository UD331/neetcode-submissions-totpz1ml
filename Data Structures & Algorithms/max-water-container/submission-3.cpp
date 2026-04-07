class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int l = 0, r = n-1, ar = 0;
        while (l < r) {
            if (heights[l] > heights[r]) {
                ar = max(ar, heights[r]*(r-l));
                r--;
            } else {
                ar = max(ar, heights[l]*(r-l));
                l++;
            }
        }
        return ar;
    }
};
