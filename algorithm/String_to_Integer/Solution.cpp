#include <string>
#include <ctype.h>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        
        int MAX_INT = 2147483647;
        int MIN_INT = -2147483648;
        if(str.size() == 0)
        	return 0;
        bool isNegtive = false;
        str = str.erase(0, s.find_first_not_of(' '));
        if(str[0] == '+'){
        	str = str.substr(1, str.length() - 1);
        }else if(str[0] == '-'){
        	str = str.substr(1, str.length() - 1);
        	isNegtive = true;
        }else if(!isdigit(str[0])){
        	return 0;
        }
        int result = 0;
        for(int i = 0; i < str.size(); i++){
        	if(isdigit(str[i])){
        		int digit = str[i] - '0';
        	    if(isNegtive){
        		   if(-result < (MIN_INT + digit) / 10){
        		   	return MIN_INT;
        		   }
        	    }else{
        	    	if(result > (MAX_INT - digit) / 10){
        	    		return MAX_INT;
        	    	}
        	    }
        	    result = result * 10 + digit;
            }
            else{
            	break;
            }
       }
       return isNegtive? -result : result;
    }
};