import java.util.Scanner;

public class Main {
    static int n;
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;
    static int[] arr;
    static int[] operator = new int[4]; 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) { //숫자 
            arr[i] = sc.nextInt(); 
        }

        for (int i = 0; i < operator.length; i++) { // 연산자 덧, 뺄 곱 나  순서 
            operator[i] = sc.nextInt();
        }
        dfs(1, arr[0]); 
        System.out.println(max);
        System.out.println(min);
    }

    // 깊이는 시작하는 지점, val은 현재 숫자 
    static void dfs(int depth, int val) { 
        if (depth == n) { // 마지막 숫자까지 갔다면 
            max = Math.max(max, val);
            min = Math.min(min, val);
            return;
        }
        
        for (int i = 0; i < operator.length; i++) {
            if (operator[i] >= 1) { // 1보다 크면 연산 수행 할때마다 하나씩 줄이기 
                operator[i]--;

                if(i == 0) { // 시작하는 지점 + 1, 맨 처음 값에 현재 값 더하기 
                    dfs(depth + 1, val + arr[depth]);
                } else if(i == 1) { // 빼기 
                    dfs(depth + 1, val - arr[depth]);
                } else if(i == 2) { // 곱하기 
                    dfs(depth + 1, val * arr[depth]);
                } else if(i == 3) { // 나누기 
                    dfs(depth + 1, val / arr[depth]);
                }

                operator[i]++; 
            }
        }
    }
}