class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int s;
        int n = numbers.size();
        for (int i = 0; i <n; i++) {
            int curr = numbers[i];
            int j = i+1;
            while(j<n) {
                int fut = numbers[j];
                if ((curr+fut) > target)
                    break;
                else if ((curr+fut)==target)
                    return {i+1,j+1};
                j+=1;
            }
        }
        return numbers;
    }
};
