class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int s = 0;
        if (n == 0)
            return 0;
        int l = 0, r = n-1;
        int lh = height[l], rh = height[r];
        while (l < r) {
            if (lh < rh) {
                                l++;

                lh = max(lh, height[l]);
                s+= lh - height[l];
            } else {
                                r--;

                rh = max(rh, height[r]);
                s+= rh - height[r];
            }

        }
        return s;
    }
};
