public class Solution {
    public int threeSumClosest(int[] nums, int target) {
           int n = nums.length;
           Arrarys.sort(nums);
           int delta = Integer.MAX_VALUE;
           int result = 0;
           for(int i = 0; i < n - 2; i++){
           	  if(i > 0 && nums[i] == nums[i - 1]){
           	  	continue;
           	  }
           	  int start = i + 1;
           	  int end = n - 1;
           	  int a = nums[i];
           	  while (start < end) {
           	  	int b = nums[start];
           	  	int c = nums[end];
           	  	if (a + b + c == target){
           	  		return target;
           	  	}
           	  	else{
           	  		if(Math.abs(a + b + c - target) < delta){
           	  			delta = Math.abs(a + b + c - target);
           	  			result = a + b + c;
           	  		}
           	  		if(a + b + c > target){
           	  			while(end > 0 && nums[end] == nums[end-1]){
           	  				end--;
           	  			}
           	  			end--;
           	  		}
           	  		else if(a + b + c < target){
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
}