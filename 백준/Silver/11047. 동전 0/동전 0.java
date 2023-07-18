
import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt(); 
		int [] arr = new int[N];
		int result = 0;
		
		//동전 배열 입력받기 오름차순
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}

		//동전 배열 역순으로 탐색 시작 -> 오름차니까,,
		//만약 동전이 값보다 크다면 넘어가고, 같거나 작다면 계산을 시작한다
		
		for(int i = N-1; i >= 0; i --) {
			
			if(arr[i] <= K) {
				result += (K/arr[i]);
				K = K % arr[i];
			}	
		}
	System.out.println(result);
	}
}
