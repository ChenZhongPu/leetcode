import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
public class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<String>();
        if(digits.length() == 0){
        	return res;
        }
        char[] cand = new char[digits.length()];
        dfs(digits, 0, cand, res);
        return res;
    }

    private void dfs(String digits, int depth, char[] cand, List<String> result){
    	Map<Character, String> m = new HashMap<Character, String>();
    	m.put('2',"abc");
    	m.put('3', "def");
    	m.put('4', "ghi");
    	m.put('5', "jkl");
    	m.put('6', "mno");
    	m.put('7', "pqrs");
    	m.put('8', "tuv");
    	m.put('9', "wxyz");
    	if(depth == digits.length()){
    		result.add(String.valueOf(cand));
    	}else{
    		String letters = m.get(digits.charAt(depth));
    		for(int i = 0; i < letters.length(); i++){
    			cand[depth] = letters.charAt(i);
    			dfs(digits, depth+1, cand, result);
    		}
    	}
    }
}