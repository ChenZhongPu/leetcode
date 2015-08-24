class Solution {
public:
    int reverse(int x) {
       bool isNegative = false;
       int magic = 214748364;
       int y = 0;
       if(x < 0){
       	  if(x == -2147483648){
       	  	return 0;
       	  }
       	  isNegative = true;
       	  x = -x;
       }
       while(x != 0){
       	int n = x % 10;
       	if(isNegative){
       		if(-y < -magic){
       			return 0;
       		}
       	}
       	else{
       		if(y > magic){
       			return 0;
       		}
       	}
       	y = y * 10 + n;
      	x = x / 10;
       }  
       return isNegative? -y : y;    
    }
};