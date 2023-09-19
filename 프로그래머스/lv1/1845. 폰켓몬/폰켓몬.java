import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>(); //Hashset 만들기
        int N = 0;
        
        for(int i = 0; i < nums.length; i++ ){
            set.add(nums[i]); //set에 순차적으로 넣어주기
        }
        
        N = set.size(); // 종류 개수
        
        if(N > nums.length/2){
            answer = nums.length/2;
        } else {
            answer = N;
        }
        

        return answer;
    }
}