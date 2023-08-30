
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	      StringTokenizer st = new StringTokenizer(br.readLine());
	      //한대, 두대, 세대에 해당하는 요금 입력 받기
	      
	      int A = Integer.parseInt(st.nextToken());
	      int B = Integer.parseInt(st.nextToken());
	      int C = Integer.parseInt(st.nextToken());
	      
	      int[] arr = new int[100]; // 입력 들어오는거 100 이하
	      int start, end = 0;
	      int first_start = 0;
	      int last_end = 0;
	      //시간을 차례로 입력 받기
	      for (int i= 0 ; i < 3; i++) {
	    	  st = new StringTokenizer(br.readLine());
	    	  start = Integer.parseInt(st.nextToken()); // 시작 시간
	    	  end = Integer.parseInt(st.nextToken()); // 끝나는 시간
	    	  
	    	  first_start = Math.min(first_start, start); // 가장 빨리 시작하는 것
	    	  last_end = Math.max(last_end, end); // 가장 늦게 끝나는 시간
	    	  
	    	  //트럭 한대의 start와 end시간만큼 배열을 더해준다. 현재 배열은 100까지 있다 
	    	  for (int j = start; j < end; j ++) {
	    		  arr[j]++; //한 트럭당 시작부터 끝까지 +1 해주기 
	    	  }
	      }
	      
	      int sum =0;
	      //가장 처음 들어온 시간 부터 가장 마지막 시간 까지 계속 계산 
	      for(int i = first_start; i < last_end; i++) {
	    	  if(arr[i] == 1) {
	    		  sum += A*arr[i];
	    	  } else if(arr[i] == 2) {
	    		  sum += B*arr[i];
	    	  } else if (arr[i] == 3) {
	    		  sum += C*arr[i];
	    	  }
	      }
	      System.out.println(sum);
	}

}
