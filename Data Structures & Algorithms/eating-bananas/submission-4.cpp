class Solution {
public:
    int time_taken (vector<int>& piles, int k) {
        int t = 0;
        for (int p:piles) {
            if (p %k == 0)
                t += int(p/k);
            else
                t +=int(p/k) +1;
        }
        return t;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
       int l = 1, r = *max_element(piles.begin(), piles.end()), res = r+1, c = 0;
       while (l<=r) {
            int m = (l+r)/2;
            int t = time_taken(piles, m);
            if (t > h)
                l = m+1;
            else {
                r = m-1;
                res = min(res, m);
                c = 1;
            }
       }
       if (c == 0)
            return -1;
        return res;
    }
};
