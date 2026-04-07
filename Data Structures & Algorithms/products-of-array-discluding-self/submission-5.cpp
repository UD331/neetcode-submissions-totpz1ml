class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1;
        bool zero = false;
        bool mult_zero = false;
        for (int n: nums) {
            if (n != 0) {
                prod *= n;
            } else {
                if (zero)
                    mult_zero = true;
                zero = true;   
            }
        }
        vector<int> r;
        for (int n: nums) {
            if (zero && n != 0)
                r.push_back(0);
            else if (zero && n == 0)
                if (mult_zero)
                    r.push_back(0);
                else
                    r.push_back(prod);
            else
                r.push_back(prod/n); 
        }
        return r;
    }
};
