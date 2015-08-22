public class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
        	return false;
        }
        int length = 0;
        int temp = x;
        while(temp > 0){
        	length++;
        	temp = temp / 10;
        } 
        if(length <= 1){
        	return true;
        }
        int i = 0;
        int rightHalf = 0;
        while(i < length / 2){
        	rightHalf = rightHalf * 10 + x % 10;
        	x = x / 10;
        	i++;
        }
        if(length % 2 == 1){
        	x = x / 10;
        }
        if(rightHalf == x){
        	return true;
        }else{
        	return false;
        }
    }
}