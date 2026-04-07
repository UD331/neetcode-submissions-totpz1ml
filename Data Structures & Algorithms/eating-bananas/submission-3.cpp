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
        int l = 1, r = *max_element(piles.begin(), piles.end()), mi = r;
        while (l <= r) { 
            int m = int((l+r)/2);
            int t = time_taken(piles, m);
            if (t<=h) {
                mi = min(mi, m);
                r = m-1;
            } else {
                l = m+1;
            }
        }
        return mi;
    }
};
