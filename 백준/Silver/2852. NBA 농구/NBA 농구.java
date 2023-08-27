
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {    // NBA 농구
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int score1 = 0, score2 = 0;
        int now = 0, answer1 = 0, answer2 = 0;
        for (int i = 0; i < N; i++)  {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int team = Integer.parseInt(st.nextToken());
            String[] tokens = st.nextToken().split(":");
            int time = 60 * Integer.parseInt(tokens[0]) + Integer.parseInt(tokens[1]);
            if (score1 > score2) {
                answer1 += time - now;
            } else if (score1 < score2) {
                answer2 += time - now;
            }
            now = time;
            if (team == 1) score1++;
            else score2++;
        }
        if (score1 > score2) {
            answer1 += 48 * 60 - now;
        } else if (score1 < score2) {
            answer2 += 48 * 60 - now;
        }
        System.out.println(String.format("%02d", answer1 / 60) + ":" + String.format("%02d", answer1 % 60));
        System.out.println(String.format("%02d", answer2 / 60) + ":" + String.format("%02d", answer2 % 60));
    }
}