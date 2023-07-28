
import java.io.*;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{		
		Stack<Integer> stack = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		

		for(int i =0 ; i < N; i ++) {
		//	br = new BufferedReader(new InputStreamReader(System.in));
			String[] arr =br.readLine().split(" "); // 공백기준으로 배열에 넣기
			
			if(arr[0].equals("push")) {
				stack.add(Integer.parseInt(arr[1]));
			} 
			
			else if(arr[0].equals("pop")) {
				if(stack.isEmpty()) {
					System.out.println(-1);
				}
				else {
					System.out.println(stack.pop( ));
				}
			}
			
			else if(arr[0].equals("size")) {
				System.out.println(stack.size());
			}
			
			else if(arr[0] .equals("empty")) {
				if(stack.isEmpty()) {
					System.out.println(1);
				}
				else {
					System.out.println(0);
				}
			}
			
			else if(arr[0].equals("top")) {
				if(stack.isEmpty()) {
					System.out.println(-1);
				}
				else {
					System.out.println(stack.peek());
				}
			}
		} //end for 
	}

}
