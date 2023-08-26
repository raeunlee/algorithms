import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        for(int i = 0; i < citations.length; i++){ // 맨앞부터 시작 
        int count = citations.length - i ; //논문 개수
            //그 인덱스 보다 큰것의 개수를 구하기

        if( citations[i] >=count){
            answer = count;
            break;
        }
         
        }
        
        return answer;
    }
}