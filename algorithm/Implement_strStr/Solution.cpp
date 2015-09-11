class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size() == 0){
        	return 0;
        }
        if(haystack.size() == 0){
        	return -1;
        }
        vector<int> match = kmpPeprocessing(needle);
        int m = haystack.size().
        int n = needle.size();
        int j = -1;
        for(int i = 0; i < m; i++){
        	while(j >=0 && haystack[i] != needle[j+1]){
        		j = match[j];
        	}
        	if(haystack[i] == needle[j+1]){
        		j++;
        	}
        	if(j == n-1){
        		return i - j;
        	}
        }
        return -1;
    }

private:
	vector<int> kmpPeprocessing(string needle){
		int n = needle.size();
		vector<int> match(n, -1);
		int j = -1;
		for(int i = 1; i < n; i++){
			while(j >= 0 && needle[i] != needle[j+1]){
				j = match[j];
			}
			if(needle[i] == needle[j+1]){
				j++;
			}
			match[i] = j;
		}
		return match;
	}
};