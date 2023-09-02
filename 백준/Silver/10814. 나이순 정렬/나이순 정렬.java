
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	      StringTokenizer st = new StringTokenizer(br.readLine()); 
	      
	      int N = Integer.parseInt(st.nextToken());
	      
	      //어레이리스트 
	      String [][]arr = new String[N][2];
	      
	      for(int i = 0; i < N; i++) {
	    	 st = new StringTokenizer(br.readLine()); //한줄받기
	    	 arr[i][0] = st.nextToken();
	    	 arr[i][1] = st.nextToken();
	      }
	      
	      //나이순(배열의 첫번째거를 기준으로 오름차순 정렬)
	        Arrays.sort(arr, new Comparator<String[]>() {
	            @Override
	            public int compare(String[] o1, String[] o2) {
	                    return Integer.parseInt(o1[0]) - Integer.parseInt(o2[0]);
	                    //반대로 뺴주면 내림차순이 됨
	            }});
	        
	        

	        for(int i = 0; i < N; i++) {
				System.out.println(arr[i][0] +" "+ arr[i][1]);
	   	 		}

	}

}
