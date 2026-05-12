class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0)
            return 0;
        int l = 0, r = height.size() - 1, ma = 0, lh = height[l], rh = height[r];
        while (l <r) {
            if (lh < rh) {
                lh = max(height[++l], lh);
                ma+= lh-height[l];
            } else {
                rh = max(height[--r], rh);
                ma+= rh-height[r];
            }
        }
        return ma;
    }
};
