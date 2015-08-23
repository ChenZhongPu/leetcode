#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int n = nums.size();
        for(int i = 0; i < n - 2; i++){
        	if(i > 0 && nums[i] == nums[i-1]){
        		continue;
        	}
        	int a = nums[i];
        	int start = i + 1;
        	int end = n - 1;
        	while(start < end){
        		int b = nums[start];
        		int c = nums[end];
        		if(a + b + c == 0){
        			vector<int> temp;
        			temp.push_back(a);
        			temp.push_back(b);
        			temp.push_back(c);
        			result.push_back(temp);
        			while(start < n - 1 && nums[start] == nums[start + 1]){
        				start++;
        			}
        			while(end > 0 && nums[end] == nums[end - 1]){
        				end--;
        			}
        			start++;
        			end--;
        		}
        		else if(a + b + c > 0){
        			while(end > 0 && nums[end] == nums[end - 1]){
        				end--;
        			}
        			end--;
        		}
        		else{
        			while(start < n - 1 && nums[start] == nums[start+ 1]){
        				start++;
        			}
        			start++;
        		}
        	}
        }
        return result;
    }
};