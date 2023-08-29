import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        List<String> list = new ArrayList<String>();
        boolean flag = true;
        
        for(int i = 0; i < words.length; i++){ // 단어를 하나씩 계속 받아들임
            if(list.contains(words[i])){ //list에 있는 단어라면?
                answer[0] = (i%n) + 1;
                answer[1] = (i/n) + 1;
                flag = false;
                break;
            }
            
            list.add(words[i]); //현재 단어 리스트에 넣기 
            
            //이전 끝단어와 현재의 첫 단어가 같지 않을 경우
            if(i>0 && words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0)){
                answer[0] = (i%n) + 1; //사람
                answer[1] = (i/n) + 1; // 순서 
                flag = false;
                break;
            }
            
        }
        if(flag) { // 만약 중간에 멈추지 않닸다면
            answer[0] = 0;
            answer[1] = 0;
            return answer;
        } 
        return answer;
    }
}