import java.util.Scanner;
import java.lang.StringBuilder;

public class WeirdAlgorithm {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    long n = sc.nextLong();
    StringBuilder str = new StringBuilder();
    str.append(n).append(" ");

    while (n != 1) {
      if (n % 2 == 0) {
        n = n / 2;
      } else {
        n = n * 3 + 1;
      }
      str.append(n).append(" ");
    }
    System.out.println(str);
  }

}