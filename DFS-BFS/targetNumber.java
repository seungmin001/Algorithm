import java.util.*;
class Solution {
    private int answer = 0;
    private int len=0;
    private int tg=0;
    
    public int solution(int[] numbers, int target) {
        len=numbers.length;
        tg=target;
        Stack<Integer> stack=new Stack<Integer>();
        stack.push(0); // 첫 원소부터 탐색 가능하도록 처음에는 영향이 없는 0만 넣는다
        dfs(stack,numbers,0,0);
        return answer;
    }
    
    //dfs에 사용할 stack, 탐색할 배열 numbers, 현재 탐색해야할 index, 여태까지 원소들의 합
    public void dfs(Stack<Integer> stack, int[] numbers, int index, int sum){        
        //가장 상위 원소 pop 후 sum에 더함
        int temp=stack.pop();
        sum+=temp;
        
        // 타겟과 비교
        if(index == len){
            if (sum == tg){
                answer++;
            }
            return;
        }
        
       //다음 원소 stack에 push
        for (int i = 0; i < 2; i++) {
            if (i==0) {
                stack.push(numbers[index]);
            } else {
                stack.push(-numbers[index]);
            }

            //다음 진행
            dfs(stack, numbers, index + 1, sum);
        }
        
    }
}
