import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] A = {1,2,3,4,5}; //5 
        int[] B = {2,1,2,3,2,4,2,5}; //8
        int[] C = {3,3,1,1,2,2,4,4,5,5}; //10
        int[] score = {0,0,0}; // 각 수포자들의 점수
        // 수포자들의 점수 계산
        for(int i=0; i < answers.length; i++) {
            if(answers[i] == A[i%5]) score[0]++;
            if(answers[i] == B[i%8]) score[1]++;
            if(answers[i] == C[i%10]) score[2]++;
        }
        
        // 최대 점수 구하기
        int max = Math.max(score[0], Math.max(score[1], score[2]));
        
        // 최대 점수를 가진 수포자 리스트 생성
        List<Integer> list = new ArrayList<Integer>();
        
        if(max == score[0])
            list.add(1);
        if(max == score[1])
            list.add(2);
        if(max == score[2])
            list.add(3);
        
        int[] answer = new int[list.size()];
        for(int i =0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}