import java.lang.StringBuilder;
import java.util.Scanner;
import java.lang.Math;

public class CoinPiles {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    StringBuilder str = new StringBuilder();
    int n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      if (Math.abs(a - b) <= Math.max(a, b) / 2 && (a + b) % 3 == 0) {
        str.append("YES").append("\n");

      } else {
        str.append("NO\n");

      }

    }
    System.out.println(str);

  }
}