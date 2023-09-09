import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;     
        // k 칸 점프 -> ans +k
        // ~현재 길이만큼 순간이동. ans 그대로
        // 건전지를 제일 적게 쓰자? 어떻게..적게쓸까요~~???
        // 도착지점에서 /2만큼 되돌아가는것도 공짜 
        while(n > 0){
            if (n%2 ==0){
                n = n/2;
            }
            else{
                n--; //하나 빼주고! 
                ans ++;
                
                n = n/2;
            }
        }
        return ans;
    }
}