#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

#define MAX_INT 2147483647
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int result = 0;
        int delta = MAX_INT;
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
        		int sum = a + b + c;
        		if(sum == target){
        			return target;
        		}
        		else{
        			if(abs(sum - target) < delta){
        				delta = abs(sum - target);
        				result = sum;
        			}
        			if(sum > target){
        				while(end > 0 && nums[end] == nums[end-1]){
        					end--;
        				}
        				end--;
        			}
        			else if(sum < target){
        				while(start < n - 1 && nums[start] == nums[start+1]){
        					start++;
        				}
        				start++;
        			}
        		}
        	}
        }
        return result;
    }
};