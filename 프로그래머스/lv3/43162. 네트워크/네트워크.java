class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[computers.length];
        
        for(int i = 0; i < computers.length; i++){
            visited[i] = false;
        }
        
        for(int i =0; i < computers.length; i++){
            if(visited[i] == false) {
                answer ++;
                dfs(i, visited, computers);
            }
        }
        
        return answer;
    }
    
    void dfs(int com, boolean[] visited, int[][] computers){
        visited[com] = true; // 방문 true
        
        for(int i = 0; i < computers.length; i++){
            if(visited[i] == false && computers[com][i]==1){
                dfs(i, visited, computers); //방문안하고 1이면
            }
        }
    }
}