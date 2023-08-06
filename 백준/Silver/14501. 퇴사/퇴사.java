
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); // 날 받기
		int[] T = new int[N + 2];
        int[] P = new int[N + 2];
        int[] dp = new int[N + 2];
        
		for(int i = 1; i <= N; i++) {
			// N만큼 반복 
			st= new StringTokenizer(br.readLine());
			T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = N ; i >0 ; i--) {
			int x = i +T[i]; // 상담 일수 
			if (x <= N + 1) // x가 범위를 초과하지 않으면 ? 
				dp[i] = Math.max(P[i] + dp[x], dp[i+1]); // 아까 세운 식
			else
				dp[i] = dp[i+1];
		}
		System.out.println(dp[1]); // 1부터 시작!!
	}
	
}