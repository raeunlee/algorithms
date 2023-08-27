import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int H;
    static int W;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        int cnt = 0; //C가 나올때 써준다
        //C 가 있는 거 찾기 
        for (int i = 0; i < H; i++) {
        	String line = br.readLine();
            for (int j = 0; j < W; j++) {
            	String x = String.valueOf(line.charAt(j)); // 한 문자씩 배열에 저장
            	
            	// 전에 C가 없고 . 일 경우
            	if (x.equals(".") && cnt == 0) {
            		System.out.print( -1 +" ");
            	}
            	// C일 경우 무조건 0출력 카운트 세주기 
            	else if ( x.equals("c")) {
            		System.out.print(0 +" ");
            		cnt = 1;
            	}
            	
            	// . 이고, 카운트도 0이 아닐 경우 
            	else if (x.equals(".") && cnt != 0) {
            		System.out.print(cnt +" ");
            		cnt ++; //C고 전 0 이 아닐 때 늘려준다
            	}
            }
            System.out.println();
            cnt = 0;  //0으로 초기화
        }

    }
}
