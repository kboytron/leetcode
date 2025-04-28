class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;

        for(int n : nums){
            count[n]++;
        }
        priority_queue<pair<int, int>> pq;
        for (auto it : count) {
            pq.push({it.second, it.first}); 
        }
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second);  
            pq.pop();
        }
        return result;

    }
};