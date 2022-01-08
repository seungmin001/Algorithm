import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        // graph
        LinkedList<ArrayList<Integer>> ll=new LinkedList<ArrayList<Integer>>();
        //visited
        ArrayList<Boolean> visited=new ArrayList<Boolean>();
        for(int i=0;i<n;i++){
            ll.add(new ArrayList<Integer>());
            visited.add(false);
        }
        //연결된 노드 저장
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i!=j && computers[i][j]==1){
                    ll.get(i).add(j);
                }
            }
        }
        //dfs
        for(int i=0;i<n;i++){
            if(dfs(ll,i,visited))
                answer+=1;
        }

        return answer;
    }
    
    public boolean dfs(LinkedList<ArrayList<Integer>> ll, int i,ArrayList<Boolean> visited){
        //System.out.println(ll.size());
        if(visited.get(i)==false){
            System.out.println(i);
            visited.set(i,true);
            for(int j:ll.get(i)){ //연결된 모든 노드에 대해 dfs
                dfs(ll,j,visited);
            }
            return true;
        }
        
        return false;
    }
}
