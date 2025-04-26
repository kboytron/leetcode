class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counter;
        for (char c : s){
            counter[c]++;
        }
        for (char c : t){
            counter[c]--;
        }
        for (auto it : counter){
            if(it.second != 0) return false;
        }
        return true;
    }
};