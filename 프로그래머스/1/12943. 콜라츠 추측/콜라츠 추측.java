class Solution {
    public int solution(int num) {
        int count = 0;
                
        while(num != 1 && count < 500){
            if (num % 2 == 1){
                num = (num * 3)  + 1;
            } else{
                num = (num / 2);
            }
            count++;
        }
    if (count >= 500) {
        return -1;
    }
   
     return count;
        
    }
}