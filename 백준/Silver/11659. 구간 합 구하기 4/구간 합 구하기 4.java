import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	static int N;
	static int M;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int[] arr = new int [N+1]; // N 만큼의 크기 
		
		// N만큼 반복 
		st= new StringTokenizer(br.readLine());
		
		for(int i = 1; i <= N; i++) {
			int tmp = Integer.parseInt(st.nextToken()); //받아오는거 계속 더해주기
			arr[i] = arr[i - 1] + tmp; //그 합을 배열에 넣어주기
			//System.out.println(arr[i]);
		}
		// M개의 줄
		
		int answer = 0; // return 할 답
		for(int i = 0 ; i < M; i++) {
			st= new StringTokenizer(br.readLine()); // 할때마다 새로운 줄 
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			answer = arr[y] - arr[x-1];
			System.out.println(answer);
		}
	}
	
	
	
}