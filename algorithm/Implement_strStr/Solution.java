public class Solution {
	private List<Integer> kmpPeprocessing(String needle){
		int n = needle.length();
		int j = -1;
		List<Integer> match = new ArrayList<Integer>();
		match.add(0, -1);
		for(int i = 1; i < n; i++){
			while(j >=0 && needle.charAt(i) != needle.charAt(j+1)){
				j = match.get(j);
			}
			if(needle.charAt(i) == needle.charAt(j+1)){
				j++;
			}
			match.add(i, j);
		}
		return match;
	}

    public int strStr(String haystack, String needle) {
        if(needle.length() == 0){
        	return 0;
        }
        if(haystack.length() == 0){
        	return -1;
        }
        List<Integer> match = kmpPeprocessing(needle);
        int m = haystack.length();
        int n = needle.length();
        int j = -1;
        for(int i = 0; i < m; i++){
        	while(j >= 0 && haystack.charAt(i) != needle.charAt(j+1)){
        		j = match.get(j);
        	}
        	if(haystack.charAt(i) == needle.charAt(j+1)){
        		j++;
        	}
        	if(j == n-1){
        		return i - j;
        	}
        }
        return -1;
    }
}