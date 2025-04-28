class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int lastIndex = 0;
        int k = 1;
        for(int i = 0; i < nums.size(); i++){
            int check = nums[i];
            if(check > nums[lastIndex]){
                lastIndex += 1;
                nums[lastIndex] = check;
                k++;
            }
            
        }
        return k;
    }
};