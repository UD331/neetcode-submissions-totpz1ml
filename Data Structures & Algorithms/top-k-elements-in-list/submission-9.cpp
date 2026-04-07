#include <queue>
#include <tuple>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue <tuple<int, int>> pq;
        unordered_map <int, int> m;
        for (int n:nums)
            if (m.count(n) != 0)
                m[n] += 1;
            else
                m[n] = 1;
        for (auto& [k,v] : m)
            pq.push({v , k});
        vector <int> r;
        for (int i = 0; i < k; i++) {
            auto [count, num] = pq.top();
            r.push_back(num);
            pq.pop();
        }
        return r;
    }
};
