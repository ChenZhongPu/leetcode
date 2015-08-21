import java.util.Map;
import java.util.HashMap;
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = {0, 0};
        Map<Integer, Integer> valueMap = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(valueMap.containsKey(nums[i])){
                valueMap.put(target - nums[i], i);
            }else{
                result[0] = valueMap.get(nums[i]) + 1;
                result[1] = i + 1;
            }
        }
        return result;
    }
}