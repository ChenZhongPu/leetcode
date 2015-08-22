#include <string>
using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() <= 1)
        	return s;
        string longest = "";
        for(int i = 0; i < s.size() - 1; i++){
        	string temp = getPalindrome(s, i, i);
        	if(temp.size() > longest.size())
        		longest = temp;
        	temp = getPalindrome(s, i, i + 1);
        	if(temp.size() > longest.size())
        		longest = temp;
        }
        return longest;
    }

private:
 	string getPalindrome(string s, int left, int right) {
 		while(left >= 0 && right < s.size() && s[left] == s[right]) {
 			left--;
 			right++;
 		}
 		return s.substr(left + 1, right - left - 1);
 	}
};