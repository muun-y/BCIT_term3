import java.util.ArrayList;

/**
 * This class provides a method to generate palindrome sequences of length N
 * using characters 'A', 'B', and 'C'.
 * 
 */
public class Lab2 {

    /**
     * Generates palindrome sequences of length N using characters 'A', 'B', and
     * 'C'.There is a base case for N = 1 and N = 2, and a general case for N > 2.
     *
     * @param N the length of the palindrome sequences to generate
     * @return an ArrayList containing all palindrome sequences of length N
     */
    public ArrayList<String> generatePalindromeSequences(int N) {
        ArrayList<String> result = new ArrayList<>();

        // Base case: N = 1
        if (N == 1) {
            result.add("A");
            result.add("B");
            result.add("C");
            return result;
        }

        // Base case: N = 2
        if (N == 2) {
            for (char c = 'A'; c <= 'C'; c++) {
                result.add(String.valueOf(c) + c);
            }
            return result;
        }

        // General case: Recursion for N > 2
        ArrayList<String> prevPalindromes = generatePalindromeSequences(N - 2);

        for (String palindrome : prevPalindromes) {
            for (char c = 'A'; c <= 'C'; c++) {
                String newPalindrome = c + palindrome + c;
                if (newPalindrome.equals(new StringBuilder(newPalindrome).reverse().toString())) {
                    result.add(newPalindrome);
                }
            }
        }

        return result;
    }
}
