import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args) throws IOException {
		  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	      StringTokenizer st = new StringTokenizer(br.readLine()); 
	      int T = Integer.parseInt(st.nextToken()); // 테스트 케이스     
	      
	      for(int i = 0; i < T; i++) {
	    	  st = new StringTokenizer(br.readLine());
	    	  int N =  Integer.parseInt(st.nextToken()); 	    	  
	    	  long arr[] = new long[N+3]; // N의 크기를 가진 배열 설정해주기
	    	  arr[0] = 1;
	    	  arr[1] =  1;
	    	  arr[2] = 1;    	 
	    	  //N이3넘을 경우 
	    	 
	    	  if(N>=3) { 
	    		  for(int j = 3; j < N; j++) {
	    		  arr[j] = arr[j-3] + arr[j-2]; //arr 3 은 arr0 + arr1
	    	  }
	    	  }
	    	System.out.println(arr[N-1]);
	      }
	}
}