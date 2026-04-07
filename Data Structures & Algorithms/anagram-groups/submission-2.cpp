#include <array>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> v;  // use string as hashable key

        for (auto& s : strs) {
            array<int, 26> count = {0};
            for (char ch : s) {
                count[ch - 'a']++;
            }
            // convert frequency array into a key string
            string key;
            for (int i = 0; i < 26; i++) {
                key += "#" + to_string(count[i]);  // separator to avoid ambiguity
            }
            v[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto& [k, group] : v) {
            result.push_back(move(group));
        }
        return result;
    }
};
