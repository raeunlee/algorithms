
//import
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] chon; // 촌
	
	static int n; //사람 수 
	static int m; //관계 수
	
	static boolean[] visited; // 방문 체크
	static int answer = -1; // 답
	
	static int start;
	static int to;
	
	public static void main(String[] args) throws Exception{
		
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			n = Integer.parseInt(br.readLine()); //한줄 
			
			chon = new ArrayList[n+1];
			visited = new boolean[n+1]; // 사람 수 + 1
			
			// 사람수만큼 ArrayList를 생성
			for (int i = 1; i <n+1; i++) {
				chon[i] = new ArrayList<>();
			}
			
			//요구하는 두 사람의 촌수 정보 받기 
			StringTokenizer st = new StringTokenizer(br.readLine()); // 토커나이저로 한줄 읽
			start = Integer.parseInt(st.nextToken()); // 탐색 시작 점 
			to = Integer.parseInt(st.nextToken()); // 탐색 끝낼점
			
			// 관계개수 
			m = Integer.parseInt(br.readLine());	
			visited = new boolean[n+1];
				
			//관계개수만큼 사람과 관계 입력받아 양방향으로 더해주기
			for(int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				chon[x].add(y);
				chon[y].add(x);
			}
			
			//시작하는 지점 찾는 지점과 카운트!!!!
			dfs(start,to,0);
			System.out.println(answer);
	}

	private static void dfs(int go, int fin, int cnt) {
		visited[go] = true; // 방문하면 일단 트루
		//구하려는 촌수의 관계의 수만큼 반복
		for(int i : chon[go]) {
			//만약 둘이 같다면 +1 촌수
			if (i == fin) {
				answer = ++cnt;
				return;
			}
			//둘이 안같고 방문안했으면
			if (!visited[i]) {
				cnt++; // 카운트 늘리고 
				dfs(i, fin , cnt); // dfs반복
				cnt --;
			}
		}
	}
}
