import java.io.*;
import java.util.*;
public class Main {
	static int n; //입력받는 가로세로 
	static int [][] map; // 2중 배열  
	static int [] dx = {-1,1,0,0}; 
	static int [] dy = {0,0,-1,1};
	static boolean[][] check; //방문한 곳은 체크하지 않음!!
	static int count; //단지 집 숫자 
	static ArrayList<Integer> zip; // 단지 집 숫자들을 저장하는 곳!! count가 하나씩 쌓임

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();

		map = new int [n][n]; 
		check = new boolean[n][n];
		
		//2중포문을 이용하여 n만큼 n번의 배열을 입력받기 
		//공백없는 숫자 입력받기!! 
		for (int i = 0; i < n; i ++ ) {
			// 임시 배열에 입력받기
			String input = sc.next();
			for(int j = 0; j < n;  j ++) {
				map[i][j] = input.charAt(j) - '0';
			}
		}
		
		count = 0 ; //0으로 일단 초기화해줌
		zip = new ArrayList<>(); // zip도 생성함
		
		// 지도를 탐색 
		for (int i = 0; i < n; i ++ ) {
			for(int j = 0; j < n;  j ++) {
				// 만약 현재 위치가 1이고 방문했다면??
				if(map[i][j] == 1 && !check[i][j]) {
					count = 1; // 일단 1이니까 1임 
					zip.add(DFS(i,j)); 
				}
			}
		}
	Collections.sort(zip);
	System.out.println(zip.size());
	for(int i : zip) {
		System.out.println(i);
	}
	}
	
	//지금 해야하는게 0이면 넘어가고 1이면 카운트를 하고 끝나면 반환해야하네,,이거어케하지 
	
	public static int DFS(int x, int y) {
		check[x][y] = true;
		for(int i = 0; i < 4; i ++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(nx >= 0 && ny >= 0 && nx < n && ny < n) {
					
				if (map[nx][ny] == 1 && !check[nx][ny]) {
					DFS(nx, ny); // 탐색
					count += 1;
				}
				
				
				//1을 발견하면 
				
			}
		}
		return count;
	}

}
