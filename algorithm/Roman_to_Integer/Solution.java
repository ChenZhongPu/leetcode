public class Solution {
    public int romanToInt(String s) {
       Map<Character, Integer> valueM = new HashMap<Character, Integer>();
       valueM.put('I', 1);
       valueM.put('V', 5);
       valueM.put('X', 10);
       valueM.put('L', 50);
       valueM.put('C', 100);
       valueM.put('D', 500);
       valueM.put('M', 1000);
       int result = valueM.get(s.charAt(0));
       for(int i = 1; i < s.length(); i++){
       	 int prev = valueM.get(s.charAt(i - 1));
       	 int curr = valueM.get(s.charAt(i));
       	 if(curr > prev){
       	 	result = result - prev + (curr - prev);
       	 }
       	 else{
       	 	result += curr;
       	 }
       }
       return result;   
    }
}