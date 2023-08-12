import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0; // 답 
        int sum = 0; // 다리위 트럭들 무게 합 
		Queue<Integer> q = new LinkedList<Integer>();
		for(int t : truck_weights) {
			while(true) {
				if(q.isEmpty()) { // 큐가 비면 삽입
					q.offer(t);
					sum += t;
					answer++;
					break;
				}
				//큐의 사이즈와 다리의 길이가 같으면 맨 처음 삽입한거 poll하고 다리 위 무게에서도 제외
				else if(q.size() == bridge_length) {
					sum -= q.poll();
				}
				else { // 다음 들어올 트럭이 최대 무게를 초과한 경우 0 을넣고 초를 증가시킴!!!!
					if(sum + t > weight) {
						q.offer(0);
						answer++;
					}
					else { // 다음 들어올 트럭이 최대 무게보다 작다면 
						q.offer(t);
						sum += t;
						answer++;
						break;
					}
				}
			}
		}
		//도합 모두가 다 걸린 시간 + 마지막 트럭의 통과시간(다리의 길이)
		return answer + bridge_length;
	}
}