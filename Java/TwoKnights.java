import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.lang.StringBuilder;
import static java.lang.Math.pow;

public class TwoKnights {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringBuilder str = new StringBuilder();
    int n = sc.nextInt();
    int a = 1;

    while (a != n + 1) {
      if (a == 1) {
        str.append(0).append("\n");

      } else if (a == 2) {
        str.append(6).append("\n");

      }
      else if (a == 3) {
        str.append(28).append("\n");

      }
      else {
        long a = (pow(n,2)*(pow(n,2) - 1) / 2)
      }
      a += 1;
    }
  }

}