
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); //버퍼리더 한줄 읽기
		
		int testcase = Integer.parseInt(st.nextToken()); //읽은것의 토큰 정수화 
		
		for(int i = 0; i <testcase; i ++ ) {
			int test = Integer.parseInt(br.readLine()); // 각각의 테스트 입력
			int [] zero = new int [41]; //40까지니깐
			int [] one = new int [41]; // 마찬가지니깐 

			// 매개변수가 0이면 0은 1, 1은 0,
			zero[0] = 1;
			zero[1] = 0;
			one[0] = 0;
			one[1] = 1;
			
			for(int k = 2; k<= test ; k++) {
				zero[k] = zero[k-1] + zero[k-2];
				one[k] = one[k-1] + one[k-2];
			}
			System.out.println(zero[test] + " " + one[test]);
			
		}
	}
}
	