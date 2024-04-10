import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Class to find the maximum benefit assignment for a given job assignment
 * problem.
 * 
 */
public class JobAssignmentFinder {

    private ArrayList<ArrayList<Integer>> benefitMatrix;

    /**
     * Reads data from a file to initialize the benefit matrix.
     *
     * @param filename The name of the file containing the input data.
     */
    public void readDataFile(final String filename) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {

            // Read the first line to determine the input size
            String sizeLine = br.readLine();
            int size = Integer.parseInt(sizeLine.trim());

            benefitMatrix = new ArrayList<>(size);

            // Read the matrix data
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.trim().split("\\s+");
                ArrayList<Integer> row = new ArrayList<>(size);
                for (String value : values) {
                    row.add(Integer.parseInt(value));
                }
                benefitMatrix.add(row);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Gets the input size of the benefit matrix.
     *
     * @return The size of the benefit matrix.
     */
    public int getInputSize() {
        return benefitMatrix.size();
    }

    /**
     * Gets the benefit matrix.
     *
     * @return The benefit matrix.
     */
    public int[][] getBenefitMatrix() {
        int[][] matrix = new int[benefitMatrix.size()][benefitMatrix.get(0).size()];
        for (int i = 0; i < benefitMatrix.size(); i++) {
            ArrayList<Integer> row = benefitMatrix.get(i);
            for (int j = 0; j < row.size(); j++) {
                matrix[i][j] = row.get(j);
            }
        }
        return matrix;
    }

    /**
     * Converts the benefit matrix to a string representation.
     *
     * @return The string representation of the benefit matrix.
     */
    public String benefitMatrixToString() {
        StringBuilder result = new StringBuilder();
        for (ArrayList<Integer> row : benefitMatrix) {
            for (Integer value : row) {
                result.append(value).append(" ");
            }
            result.append("\n");
        }
        return result.toString();
    }

    /**
     * Finds the maximum assignment of jobs to persons.
     *
     * @return The list representing the maximum assignment.
     */
    public ArrayList<Integer> getMaxAssignment() {
        ArrayList<ArrayList<Integer>> allAssignments = getPermutations(getInputSize());
        int maxBenefit = Integer.MIN_VALUE;
        ArrayList<Integer> maxAssignment = null;

        for (ArrayList<Integer> assignment : allAssignments) {
            int totalBenefit = 0;
            for (int i = 0; i < assignment.size(); i++) {
                int jobIndex = assignment.get(i);
                totalBenefit += getBenefit(i, jobIndex); // Utilize getBenefit method
            }
            if (totalBenefit > maxBenefit) {
                maxBenefit = totalBenefit;
                maxAssignment = new ArrayList<>(assignment); // Ensure a deep copy is made
            }
        }

        return maxAssignment;
    }

    /**
     * Gets the total benefit value of the maximum assignment.
     *
     * @return The total benefit value of the maximum assignment.
     */
    public int getMaxAssignmentTotalValue() {
        ArrayList<Integer> maxAssignment = getMaxAssignment();
        int totalValue = 0;
        if (maxAssignment != null) {
            for (int i = 0; i < maxAssignment.size(); i++) {
                int person = i;
                int job = maxAssignment.get(i);
                totalValue += getBenefit(person, job);
            }
        }
        return totalValue;
    }

    /**
     * Gets the benefit of a person for a particular job.
     *
     * @param person The index of the person.
     * @param job    The index of the job.
     * @return The benefit of the person for the job.
     */
    public int getBenefit(int person, int job) {
        return benefitMatrix.get(person).get(job);
    }

    /**
     * Recursive decrease-and-conquer algorithm to generate a list of all
     * permutations of the numbers 0..N-1. This follows the "decrease by 1" pattern
     * of decrease and conquer algorithms.
     * 
     * This method returns an ArrayList of ArrayLists. One permutation is an
     * ArrayList containing 0,1,2,...,N-1 in some order. The final result is an
     * ArrayList containing N! of those permutations.
     * 
     * @param N
     * @return
     */
    private ArrayList<ArrayList<Integer>> getPermutations(int N) {
        ArrayList<ArrayList<Integer>> results = new ArrayList<ArrayList<Integer>>();

        /**
         * This isn't a "base case", it's a "null case". This function does not call
         * itself with an argument of zero, but we can't prevent another caller from
         * doing so. It's a weird result, though. The list of permutations has one
         * permutation, but the one permutation is empty (0 elements).
         */
        if (N == 0) {
            ArrayList<Integer> emptyList = new ArrayList<Integer>();
            results.add(emptyList);

        } else if (N == 1) {
            /**
             * Now THIS is the base case. Create an ArrayList with a single integer, and add
             * it to the results list.
             */
            ArrayList<Integer> singleton = new ArrayList<Integer>();
            singleton.add(0);
            results.add(singleton);

        } else {
            /**
             * And: the main part. First a recursive call (this is a decrease and conquer
             * algorithm) to get all the permutations of length N-1.
             */
            ArrayList<ArrayList<Integer>> smallList = getPermutations(N - 1);

            /**
             * Iterate over the list of smaller permutations and insert the value 'N-1' into
             * every permutation in every possible position, adding each new permutation to
             * the big list of permutations.
             */
            for (ArrayList<Integer> perm : smallList) {

                /**
                 * Add 'N-1' -- the biggest number in the new permutation -- at each of the
                 * positions from 0..N-1.
                 */
                for (int i = 0; i < perm.size(); i++) {
                    ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                    newPerm.add(i, N - 1);
                    results.add(newPerm);
                }

                /**
                 * Add 'N-1' at the end (i.e. at position "size").
                 */
                ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                newPerm.add(N - 1);
                results.add(newPerm);

            }

        }

        /**
         * Nothing left to do except:
         */
        return results;
    }
}