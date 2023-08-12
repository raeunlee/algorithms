import java.util.*;
class Solution {  
   public int solution(int[][] land) {
       //행이 4개 - 각 행 마다 max값 더해주기
       for(int i=1; i<land.length; i++){
           //각행에 이전행의 최댓값을 구해서 더해줌. 근데 0열엔 앞서 1,2,3 열의 최댓값중 하나만 올 수 있음
           land[i][0] += Math.max(Math.max(land[i-1][1], land[i-1][2]), land[i-1][3]);
            // 나머지 행도 똑같이 진행해준다
           land[i][1] += Math.max(Math.max(land[i-1][0], land[i-1][2]), land[i-1][3]);
           land[i][2] += Math.max(Math.max(land[i-1][1], land[i-1][0]), land[i-1][3]);
           land[i][3] += Math.max(Math.max(land[i-1][1], land[i-1][2]), land[i-1][0]);
       }

       // 모든 작업이 끝난 후,, sort로 최댓값부터 나열 
       int[] answer = land[land.length-1];
       Arrays.sort(answer);

       // 가장 큰 값을 내보낸다
       return answer[answer.length-1];
   }
}