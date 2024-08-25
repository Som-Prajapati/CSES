import java.util.Scanner;

public class IncreasingArray {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    long[] array = new long[n];
    long steps = 0;
    for (int i = 0; i < array.length; i++) {
      array[i] = sc.nextLong();
    }
    for (int i = 0; i < array.length - 1; i++) {
      if (array[i] > array[i + 1]) {
        steps += array[i] - array[i + 1];
        array[i + 1] = array[i];
      }
    }
    System.out.println(steps);
  }
}