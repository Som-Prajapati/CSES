import java.util.Scanner;

public class Repetitions {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    char[] array = str.toCharArray();
    long count = 1;
    long count_max = 1;
    for (int i = 0; i < array.length - 1; i++) {
      if (array[i] == array[i + 1]) {
        count += 1;
      } else {
        count = 1;
      }
      if (count_max < count) {
        count_max = count;
      }
    }
    System.out.println(count_max);
  }
}