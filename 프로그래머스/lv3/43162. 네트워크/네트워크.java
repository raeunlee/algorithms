import java.util.*;

class Solution {
    Queue<Integer> q = new LinkedList<>();
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n]; 
        
        for(int i =0; i < computers.length; i++){
            if(visited[i] == false) { // default
                bfs(i, visited, computers);     
                answer ++;
            }
        }
        return answer;
    }
    
   void bfs(int com, boolean[]visited, int[][] computers){
        q.offer(com);
        visited[com] = true;
        while(!q.isEmpty()){
            int value = q.poll();// 빼낸게 
            for(int i = 0; i < computers.length; i ++) { // 네트워크만큼 ㄱ
                if (visited[i] == false && computers[value][i]==1){
                    //1이거나 방문안한거있으면 
                    visited[i] = true; // 방문처리 
                    q.add(i); // 다시 더해준다,, 무한반복
                }
            }
        }
    }
    
//     void dfs(int com, boolean[] visited, int[][] computers){
//         visited[com] = true; // 방문 true
        
//         for(int i = 0; i < computers.length; i++){
//             if(visited[i] == false && computers[com][i]==1){
//                 dfs(i, visited, computers); //방문안하고 1이면
//             }
//         }
//     }
    

}