import java.util.HashMap;

/**
 * A lab assginment for calculating binomial coefficients using recursive and
 * dynamic programming techniques.
 * 
 * @author Mun Young Cho(setC - A01330048)
 */
public class Lab6 {

    private HashMap<String, Long> memo;

    /**
     * Constructs a Lab6 object with an empty memoization table.
     */
    public Lab6() {
        memo = new HashMap<>();
    }

    /**
     * Calculates the binomial coefficient using a recursive approach.
     *
     * @param m The first parameter of the binomial coefficient.
     * @param n The second parameter of the binomial coefficient.
     * @return The calculated binomial coefficient value.
     */
    public long SW_Recursive(int m, int n) {
        if (m == 0 || n == 0) {
            return 1;
        }

        String key = m + "," + n;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        long result = SW_Recursive(m - 1, n) + SW_Recursive(m, n - 1);
        memo.put(key, result);
        return result;
    }

    /**
     * Runs the SW_Recursive method for a range of input values and measures the
     * execution time.
     *
     * @param lowerBound The lower bound of the input range.
     * @param upperBound The upper bound of the input range.
     */
    public void RunRecursive(int lowerBound, int upperBound) {
        for (int i = lowerBound; i <= upperBound; i++) {
            long startTime = System.nanoTime();
            long result = SW_Recursive(i, i);
            long endTime = System.nanoTime();
            long durationMs = (endTime - startTime) / 1_000_000;
            System.out.println("SW_Recursive(" + i + "," + i + ") = " + result + ", time is " + durationMs + " ms");
        }
    }

    /**
     * Calculates the binomial coefficient using dynamic programming.
     *
     * @param m The first parameter of the binomial coefficient.
     * @param n The second parameter of the binomial coefficient.
     * @return The calculated binomial coefficient value.
     */
    public long SW_DynamicProg(int m, int n) {
        long[][] dp = new long[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }

        return dp[m][n];
    }

    /**
     * Runs the SW_DynamicProg method for a range of input values and measures the
     * execution time.
     *
     * @param lowerBound The lower bound of the input range.
     * @param upperBound The upper bound of the input range.
     */
    public void RunDynamicProg(int lowerBound, int upperBound) {
        for (int i = lowerBound; i <= upperBound; i++) {
            long startTime = System.nanoTime();
            long result = SW_DynamicProg(i, i);
            long endTime = System.nanoTime();
            long durationMs = (endTime - startTime) / 1_000_000;
            System.out.println("SW_DynamicProg(" + i + "," + i + ") = " + result + ", time is " + durationMs + " ms");
        }
    }
}
