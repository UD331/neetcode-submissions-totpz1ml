class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0)
            return 0;
        int l = 0, r = height.size()-1, ma = 0;
        int lh = height[l], rh = height[r];
        while (l<r) {
            if (lh < rh) {
                l++;
                lh = max(lh, height[l]);
                ma += lh - height[l];
            } else {
                r--;
                rh = max(rh, height[r]);
                ma += rh- height[r];
            }
            
        }
        return ma;
    }
};
