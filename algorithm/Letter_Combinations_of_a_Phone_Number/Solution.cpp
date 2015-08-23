#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.size() == 0){
        	return res;
        }
        string cand = "";
        dfs(digits, 0, cand, res);
        return res;
    }

private:
	void dfs(string digits, int depth, string cand, vector<string> &result){
		map<char,string> m;
		m['2'] = "abc"; m['3'] = "def"; m['4'] = "ghi";
		m['5'] = "jkl"; m['6'] = "mno"; m['7'] = "pqrs";
		m['8'] = "tuv"; m['9'] = "wxyz";
		if(depth == digits.size()){
			result.push_back(cand);
		}
		else{
			string letters = m[digits[depth]];
			for(int i = 0; i < letters.size(); i++){
				cand = cand + letters[i];
				dfs(digits, depth+1, cand, result);
				cand = cand.substr(0, cand.size() - 1);
			}
		}
	}
};