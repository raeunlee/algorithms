import java.util.Scanner;
public class Main {
	static String S;
	public static void main(String[] args) {
		 Scanner sc = new Scanner(System.in);
	     String str = sc.next().toUpperCase(); // 미리 대문자로 받는다 
		 int[] arr = new int [26]; // 알파벳은 총 26개	
		 int max = 0; // 최대 반복 횟수
		 char result = 0; // 결과
	  // 사용된 알파벳의 배열에 1씩 증가시킨다.
		 for (int i = 0; i < str.length(); i++) {
				arr[str.charAt(i) - 65]++; // 받아온문자열의 각 글자에서 65를 뺀다
				if (max < arr[str.charAt(i) - 65]) { // max는 0 으로 두고 0보다 큰값이 있다면 
					max = arr[str.charAt(i) - 65]; // max를 최댓값으로 두고 이를 계속 반복함!
					result = str.charAt(i); //결과를 해당 문자로 둔다 
					// 만약 최대값이 중복된다면 물음표 출력한다
				} else if (max == arr[str.charAt(i) - 65]) {
					result = '?';
				}
			}
	       System.out.println(result);
		}
}
