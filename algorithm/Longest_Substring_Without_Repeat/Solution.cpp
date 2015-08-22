#include <map>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int lastRepeatPos = -1;
        int length = 0;
        map<char, int> m;
        for(int i = 0; i < s.size(); i++){
        	if(m.find(s[i]) != m.end() && lastRepeatPos < m[s[i]]){
        		lastRepeatPos = m[s[i]];
        	}
        	if(i - lastRepeatPos > length){
        		length = i - lastRepeatPos;
        	}
        	m[s[i]] = i;
        }
        return length;
    }
};