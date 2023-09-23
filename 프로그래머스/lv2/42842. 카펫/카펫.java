class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int x = 0; //가로 
        int y = 0; //세로       
        //가로가 brown/2보다 클수없음!
        for(int i = 1; i < brown/2; i++){
            x = i;
            for(int j = 0; j <= i; j ++) { //y는 항상 x보다 작거나같음
               y = j; 
                int brown_lim = 2*x+ 2*y - 4;
                int yellow_lim = (x-2) * (y-2);
                int gatsu = brown + yellow;
                int hap = x * y;
                if(brown_lim == brown && yellow_lim >= yellow && hap == gatsu) {
                    x = i;
                    y = j;                    
                    answer[0] = x;
                    answer[1] = y;
                }
            }
        }
        
        return answer;
    }
}