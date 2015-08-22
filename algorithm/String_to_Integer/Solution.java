
public class Solution {
    public static int MAX_INT = 2147483647;
    public static int MIN_INT = -2147483648;
    public int myAtoi(String str) {
        if(str == null || str.length() == 0)
            return 0;
        boolean isNegtive = false;
        str = str.trim();
        if(str.charAt(0) == '+'){
            str = str.substring(1, str.length());
        }else if(str.charAt(0) == '-'){
            str = str.substring(1, str.length());
            isNegtive = true;
        }else if(!Character.isDigit(str.charAt(0))){
            return 0;
        }
        int result = 0;
        for(int i = 0; i < str.length(); i++){
            if(Character.isDigit(str.charAt(i))){
                if(isNegtive){
                    if(-result < ( MIN_INT + Character.getNumericValue(str.charAt(i))) / 10){
                        return MIN_INT;
                    }
                }
                else{
                    if(result > (MAX_INT - Character.getNumericValue(str.charAt(i))) / 10){
                        return MAX_INT;
                    }
                }
                result = result * 10 + Character.getNumericValue(str.charAt(i));
            }
            else{
                break;
            }
        }
        return isNegtive? -result : result;
    }
}