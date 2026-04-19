#include <queue>
#include <tuple>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        
        // Count frequencies
        for (int n : nums)
            freq[n]++;
        
        priority_queue<pair<int,int>> pq;
        vector<int> result;
        for (auto& entry : freq) {
            pq.push({-entry.second, entry.first});
            if (pq.size() > k)
                pq.pop();
        }
        for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        
        return result;
    
    }
};
