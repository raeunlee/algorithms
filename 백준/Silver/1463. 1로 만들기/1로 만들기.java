import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		// 주어지는 정수 N
		int N = sc.nextInt();

		int[] dp = new int[N+1];
		
		dp[1] = 0; // 1일 경우 연산 필ㅇ요없으니 0 
		
		for(int i = 2; i<=N; i++) {
			dp[i] = dp[i-1] + 1;
			
			if(i%2 == 0) { // 2로 나누어 떨어질 경우 
				dp[i] = Math.min(dp[i], dp[i/2] +1);  // 둘중 작은 값 return
			}
			
			if(i%3 == 0) { // 2로 나누어 떨어질 경우 
				dp[i] = Math.min(dp[i], dp[i/3] +1);  // 둘중 작은 값 return
			}
		}
			System.out.println(dp[N]);
	}
}
