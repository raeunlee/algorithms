// import java.util.*;

// class Solution
// {
//     public int solution(int []A, int []B)
//     {
//         ArrayList<Integer> arrA = new ArrayList<Integer>();
        
//         ArrayList<Integer> arrB = new ArrayList<Integer>();
//         //ArrayList에 더해주기
//         for(int i = 0; i < A.length; i++){
//             arrA.add(A[i]);
//             arrB.add(B[i]);
//         }
        
//         Collections.sort(arrA);
//         Collections.sort(arrB);
//         Collections.reverse(arrB);
//         int answer = 0;
//         for(int i = 0; i < A.length; i++){
//             answer += arrA.get(i) * arrB.get(i);
//         }

//         return answer;
//     }
// }

import java.util.Collections;
import java.util.PriorityQueue;

class Solution
{
    public static int solution(int[] A, int[] B) {
        int ans = 0;
        PriorityQueue<Integer> a = new PriorityQueue<>();
        PriorityQueue<Integer> b = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < A.length; i++) {
            a.add(A[i]);
            b.add(B[i]);
        }

        while (!a.isEmpty()) {
            ans += a.poll() * b.poll();
        }

        return ans;
    }
}