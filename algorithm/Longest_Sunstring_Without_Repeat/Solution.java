import java.util.Map;
import java.util.HashMap;
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lastRepeatPos = -1;
        int length = 0;
        Map<Character, Integer> m = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++){
            if(m.containsKey(s.charAt(i)) && lastRepeatPos < m.get(s.charAt(i))){
                lastRepeatPos = m.get(s.charAt(i));
            }
            if(i - lastRepeatPos > length){
                length = i - lastRepeatPos;
            }
            m.put(s.charAt(i), i);
        }
        return length;
    }
}