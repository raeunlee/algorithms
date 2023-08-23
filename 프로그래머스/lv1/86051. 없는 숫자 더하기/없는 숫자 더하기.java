import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int tmp = 0; 
        for(int i : numbers) {
            tmp += i;
        }
        for(int i = 0; i< 10; i++){
           answer += i;
        }
        answer -= tmp;
        return answer;
    }
}