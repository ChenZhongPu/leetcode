class Solution {
public:
    int romanToInt(string s) {
        map<char,int> valueM;
        valueM['I'] = 1;
        valueM['V'] = 5;
        valueM['X'] = 10;
        valueM['L'] = 50;
        valueM['C'] = 100;
        valueM['D'] = 500;
        valueM['M'] = 1000;
        int result = valueM[s[0]];
        for(int i = 1; i < s.size(); i++){
        	int prev = valueM[s[i-1]];
        	int curr = valueM[s[i]];
        	if(curr > prev){
        		result = result - prev + (curr - prev);
        	}
        	else{
        		result += curr;
        	}
        }
        return result;
    }
};