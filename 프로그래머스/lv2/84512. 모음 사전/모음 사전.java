class Solution {
	public int solution(String word) {
		String str = "AEIOU";
		int[] x = {781,156,31,6,1}; // 1 ~ 5 자릿수 경우의수
		int result = word.length();
        int index = 0;
        
        //글자 전체 길이만큼 반복
		for(int i=0;i<word.length();i++){      
            // 단어가 AEIOU중 몇번쨰 인덱스인지 구한다 
			index = str.indexOf(word.charAt(i));
            // 그 인덱스에 해당하는 자릿수를 곱하여 계산한다
			result+=x[i]*index;
		}
		return result;
	}
}