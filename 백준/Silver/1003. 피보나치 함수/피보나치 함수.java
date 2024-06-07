import java.util.*;
import java.io.*;

public class Main {
    static int count_0, count_1;
    static int fibonacci(int n)
    {
        if (n == 0)
        {
            count_0++;
            return 0;
        }

        else if (n == 1)
        {
            count_1++;
            return 1;
        }

        else return fibonacci(n - 1) + fibonacci(n - 2);
    }
    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++)
        {
            int N = Integer.parseInt(in.readLine());
            int zero = 1;
            int one = 0;
            int zero_plus_one = 1;
            for (int j = 0; j < N; j++)
            {
                zero = one;
                one = zero_plus_one;
                zero_plus_one = one + zero;
            }

            System.out.println(zero + " " + one);
        }
    }
}