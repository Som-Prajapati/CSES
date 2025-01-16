
// import java.util.Scanner;
// import java.lang.StringBuilder;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class NumberSpiral {
  public static void main(String[] args) {
    try {
      // Scanner sc = new Scanner(System.in);
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      StringTokenizer input1 = new StringTokenizer(br.readLine());

      long n = Long.parseLong(input1.nextToken());
      long a = 0;

      // int n = sc.nextInt();
      // long[] result = new long[n];
      // StringBuilder str = new StringBuilder();
      // long[] arr_x = new long[n];
      // long[] arr_y = new long[n];

      for (int i = 0; i < n; i++) {
        StringTokenizer input = new StringTokenizer(br.readLine());

        // arr_x[i] = sc.nextLong();
        // arr_y[i] = sc.nextLong();
        // long x = sc.nextLong();
        // long y = sc.nextLong();

        long x = Long.parseLong(input.nextToken());
        long y = Long.parseLong(input.nextToken());

        if (x > y) {
          if (x % 2 != 0) {
            a = (x - 1) * (x - 1) + y;
          } else {
            a = ((x * x + 1 - y));
          }
        } else {
          if (y % 2 == 0) {
            a = ((y - 1) * (y - 1) + x);
          } else {
            a = ((y * y + 1 - x));
          }
        }
        bw.write(Long.toString(a));
        bw.newLine();
      }
      // System.out.println(str);
      // for (long l : result) {
      // System.out.println(l);
      // }
      // sc.close();
      bw.flush();
      bw.close();
      // br.close();
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

}