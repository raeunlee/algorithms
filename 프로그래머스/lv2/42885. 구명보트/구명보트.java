import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people); // 작은거부터 차례대로 
        int index = 0; // 최솟값의 역할을 한다 
        //최댓값부터 시작한다
        //최솟값이 최댓값보다 커지면 바로 종료한다
        for (int i = people.length - 1; i >= index; i--) {
            if (people[i] + people[index] <= limit) {
                //가장 작은 + 큰게 무게합을 안넘는다면?
                index++; // 가장 작은 사람 보냈으니 그다음 작은사람을 최솟값으로 둔다 
                answer++; // 둘이 같이 가고 
            }
            else {
                answer++;
            }
        }
        return answer;
    }
}
 