import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int n = nums.length;
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
        		if(a + b + c == 0){
        			ArrayList<Integer> temp = new ArrayList<Integer>();
        			temp.add(a);
        			temp.add(b);
        			temp.add(c);
        			result.add(temp);
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
        		}else{
        			while(start < n - 1 && nums[start] == nums[start + 1]){
        				start++;
        			}
        			start++;
        		}
        	}
        }
        return result;
    }
}