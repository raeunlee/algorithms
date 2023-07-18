
import java.util.Scanner;

public class Main {
	
	static int N;
	static int result;
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		result = 0;
		// N/5 가 1이상이라면? 
		
		while(true) {
			if(N%5 == 0) { // 5로나누어지는 경우 
				result += N/5; 
				N = N%5;
				System.out.println(result);
				break;
			}
			if(N<0) {
				System.out.println(-1);
				break;
			}
			else {
			N = N - 3;
			result += 1;
			}
			
		}
	}
}
