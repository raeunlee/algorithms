// 공백문자가 여러개 오면 split 오류 나옴 -> StringToknizer사용할 것 
// StringTokenizer(String str, String delim, boolean flag) : flag는 구분자 자체도 토큰으로 인식하게 할지 여부를 정한다. 
import java.util.*;

class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        
        // s를 공백기준으로, 공백포함하여 파싱하기 
        StringTokenizer st = new StringTokenizer(s, " ", true);
		StringBuilder sb = new StringBuilder();
        
        
        while(st.hasMoreTokens()) {
            String word = st.nextToken();
            if(word.equals(" "))
                sb.append(word);
            else
                sb.append(word.substring(0,1).toUpperCase() + word.substring(1));
        }
        
        return sb.toString();
    }
}