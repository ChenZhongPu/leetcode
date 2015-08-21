public class Solution {
    public String convert(String s, int numRows){
        if(numRows <= 1 || numRows >= s.length())
        {
            return s;
        }
        int row = 0;
        int step = 1;
        String[] result = new String[numRows];
        for(int i = 0; i < s.length(); i++){
            if(row == numRows - 1)
                step = -1;
            else if(row == 0)
                step = 1;
            if(result[row] == null) result[row] = String.valueOf(s.charAt(i));
            else
              result[row] = result[row] + s.charAt(i);
            row += step;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < numRows; i++){
            sb.append(result[i]);
        }
        return sb.toString();
    }
}