import java.util.Scanner;
import java.lang.StringBuilder;

public class Permutations {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    long n = sc.nextInt();
    StringBuilder str = new StringBuilder();
    if (n == 2 | n == 3) {
      System.out.println("NO SOLUTION");
      return;
    }
    for (long i = 2; i < n + 1; i += 2) {
      str.append(i).append(" ");
    }
    for (long i = 1; i < n + 1; i += 2) {
      str.append(i).append(" ");
    }
    System.out.println(str.toString());
  }
}