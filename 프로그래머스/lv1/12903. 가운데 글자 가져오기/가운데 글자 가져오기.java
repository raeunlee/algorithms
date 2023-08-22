import java.io.*;

class Solution {
    public String solution(String s) {
        String answer = "";
       // StringBuilder sb = new StringBuilder();
        
        String tmp[] = s.split("");    
        
        if (tmp.length % 2 != 0) { // 홀수면 
            answer = tmp[tmp.length/2];
        }
        else{
            answer = tmp[tmp.length/2-1] + tmp[tmp.length/2];
        }
        
        return answer;
    }
}