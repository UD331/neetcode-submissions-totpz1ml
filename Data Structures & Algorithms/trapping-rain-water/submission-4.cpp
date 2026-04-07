class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0)
            return 0;
        int l = 0, r = height.size() - 1, ma = 0, lh = height[l], rh = height[r];
        while (l <r) {
            if (height[l] < height[r]) {
                lh = max(lh, height[l]);
                ma += lh - height[l];
                l++; 
            } else {
                rh = max(rh, height[r]);
                ma += rh - height[r];
                r--; 
            }
        }
        return ma;
    }
};
