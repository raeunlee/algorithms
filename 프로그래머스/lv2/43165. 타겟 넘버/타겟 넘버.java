class Solution {
    int[] numbers;
    int target;
    int answer;
    
    void dfs(int index, int sum){
        
        if (index == numbers.length){
            if (sum == target) { answer ++;
                return; // 탈출
            }
        }
        
        // index가 전체길이 보다 커지면 return
        if (index >= numbers.length) {
            return;
        }
        
        //수행동작 
        dfs(index + 1 , sum + numbers[index]);
        dfs(index + 1, sum - numbers[index]);
    }
    
    public int solution(int[] numbers, int target) {
        answer = 0;
        this.numbers = numbers;
        this.target = target;      
        dfs(0,0); 
        return answer;
    }

}