public class Solution {
	private String getPalindrome(String s, int left, int right){
		while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
			left--;
			right++;
		}
		return s.substring(left + 1, right);
	}

    public String longestPalindrome(String s) {
    	if (s.length() == 1)
    		return s;
        String longest = "";
        for(int i = 0; i < s.length() - 1; i++){
        	String temp = this.getPalindrome(s, i, i);
        	if(temp.length() > longest.length()){
        		longest = temp;
        	}
        	temp = this.getPalindrome(s, i, i + 1);
        	if(temp.length() > longest.length()){
        		longest = temp;
        	}
        }
        return longest;
    }
}