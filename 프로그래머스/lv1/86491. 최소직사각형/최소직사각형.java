import java.util.*;
// 가로세로 중 큰거는 가로에 작은거는 세로에 두고
// 그 중에서 가장 큰 것을 뽑아내기
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] < sizes[i][1]){//가로가 세로보다 작으면 자리 바꾸기
                int tmp = sizes[i][0];
                System.out.println(tmp);
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        
        int garo = 0; 
        for(int i = 0; i< sizes.length; i++){
            if(sizes[i][0] > garo) {
                garo = sizes[i][0]; // 큰 값으로 교체
            }
        }
      //  System.out.println(garo);
        int sero = 0; 
        for(int i = 0; i<sizes.length; i++){
            if(sizes[i][1] > sero) {
                sero = sizes[i][1]; // 큰 값으로 교체
            }
        }
      //  System.out.println(sero);
        answer = garo * sero;
        return answer;
    }
}