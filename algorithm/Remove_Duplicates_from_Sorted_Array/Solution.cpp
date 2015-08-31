class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0){
        	return 0;
        }
        int j = 0;
        for(int i = 0; i < nums.size(); i++){
        	if(nums[i] != nums[j]){
        		nums[j + 1] = nums[i];
        		j++;
        	}
        }
        return j + 1;
    }
};