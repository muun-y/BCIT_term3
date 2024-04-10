import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * The JobAssignmentFinder class is responsible for finding the optimal
 * assignment of jobs to persons based on a benefit matrix. It provides methods
 * to read data from a file, calculate the maximum benefit assignment, calculate
 * the greedy assignment, and determine the total values of the assignments.
 * 
 */
public class JobAssignmentFinder {

	/**
	 * This data is the input to the problem; it will be read from a data file.
	 */
	private int[][] benefitMatrix;
	private int problemSize;
	private ArrayList<Integer> maxAssignment;
	private int maxAssignmentTotalValue;

	/**
	 * Reads the data file and stores the benefit matrix data for subsequent use.
	 * 
	 * @param fileName
	 */
	public void readDataFile(String fileName) throws FileNotFoundException {
		File file = new File(fileName);
		Scanner sc = new Scanner(file);
		this.problemSize = sc.nextInt();
		this.benefitMatrix = new int[this.problemSize][this.problemSize];
		for (int r = 0; r < this.problemSize; r++) {
			for (int c = 0; c < this.problemSize; c++) {
				this.benefitMatrix[r][c] = sc.nextInt();
			}
		}
		sc.close();
	}

	/**
	 * Basic getter for the problem size aka "N".
	 * 
	 * @return
	 */
	public int getInputSize() {
		return this.problemSize;
	}

	/**
	 * Basic getter for the benefit matrix (input).
	 * 
	 * @return
	 */
	public int[][] getBenefitMatrix() {
		return this.benefitMatrix;
	}

	/**
	 * Returns a string representation of the (input) benefit matrix.
	 * 
	 * @return
	 */
	public String benefitMatrixToString() {
		StringBuilder result = new StringBuilder();
		result.append("Matrix size is ").append(this.problemSize).append(" x ").append(this.problemSize).append("\n");
		for (int[] row : this.benefitMatrix) {
			result.append("[");
			for (int i = 0; i < this.problemSize - 1; i++) {
				result.append(row[i]).append(" ");
			}
			result.append(row[this.problemSize - 1]).append("]\n");
		}
		return result.toString();
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
		ArrayList<ArrayList<Integer>> results = new ArrayList<>();
		if (N == 0) {
			results.add(new ArrayList<>());
		} else if (N == 1) {
			ArrayList<Integer> singleton = new ArrayList<>();
			singleton.add(0);
			results.add(singleton);
		} else {
			ArrayList<ArrayList<Integer>> smallList = getPermutations(N - 1);
			for (ArrayList<Integer> perm : smallList) {
				for (int i = 0; i < perm.size(); i++) {
					ArrayList<Integer> newPerm = new ArrayList<>(perm);
					newPerm.add(i, N - 1);
					results.add(newPerm);
				}
				ArrayList<Integer> newPerm = new ArrayList<>(perm);
				newPerm.add(N - 1);
				results.add(newPerm);
			}
		}
		return results;
	}

	/**
	 * Helper function determines the total value of making the given job
	 * assignment.
	 * 
	 * @return
	 */
	private int checkValueOfAssignment(ArrayList<Integer> jobAssignment, int[][] benefitMatrix) {
		int total = 0;
		for (int person = 0; person < jobAssignment.size(); person++) {
			int job = jobAssignment.get(person);
			total += benefitMatrix[person][job];
		}
		return total;
	}

	/**
	 * Calculates the maximum assignment based on all permutations of the benefit
	 * matrix.
	 * Updates the maxAssignment and maxAssignmentTotalValue fields accordingly.
	 */
	private void calculateMaxAssignment() {
		ArrayList<ArrayList<Integer>> allPermutations = getPermutations(this.benefitMatrix.length);
		int maxBenefit = 0;
		for (ArrayList<Integer> jobAssignment : allPermutations) {
			int benefit = checkValueOfAssignment(jobAssignment, this.benefitMatrix);
			if (benefit > maxBenefit) {
				maxBenefit = benefit;
				this.maxAssignment = jobAssignment;
			}
		}
		this.maxAssignmentTotalValue = maxBenefit;
	}

	/**
	 * Do exhaustive search to find the maximum-valued assignment of jobs to people.
	 * This blindly performs the entire exhaustive search, even if this has already
	 * been done before on the current data set. It would (obvs) be smarter to
	 * "save" the result any time we calculate it, in order to avoid this
	 * recalculation. Oh well.
	 * 
	 * @return
	 */
	public ArrayList<Integer> getMaxAssignment() {
		if (this.maxAssignment == null) {
			calculateMaxAssignment();
		}
		return this.maxAssignment;
	}

	/**
	 * Return the total value of the max assignment. This blindly performs the
	 * entire exhaustive search, even if this has already been done before. It would
	 * (obvs) be smarter to "save" the result any time we calculate it, in order to
	 * avoid this recalculation. Oh well.
	 * 
	 * @return
	 */
	public int getMaxAssignmentTotalValue() {
		if (this.maxAssignment == null) {
			calculateMaxAssignment();
		}
		return this.maxAssignmentTotalValue;
	}

	/**
	 * Calculates the greedy assignment of jobs to persons based on the benefit
	 * matrix.
	 * The greedy assignment algorithm selects the job with the highest benefit for
	 * each person,
	 * ensuring that no job is assigned to more than one person.
	 *
	 * @return ArrayList<Integer> representing the greedy assignment of jobs to
	 *         persons.
	 */
	public ArrayList<Integer> getGreedyAssignment() {
		ArrayList<Integer> greedyAssignment = new ArrayList<>();
		boolean[] jobAssigned = new boolean[this.problemSize];
		for (int person = 0; person < this.problemSize; person++) {
			int maxBenefit = Integer.MIN_VALUE;
			int assignedJob = -1;
			for (int job = 0; job < this.problemSize; job++) {
				if (!jobAssigned[job] && this.benefitMatrix[person][job] > maxBenefit) {
					maxBenefit = this.benefitMatrix[person][job];
					assignedJob = job;
				}
			}
			jobAssigned[assignedJob] = true;
			greedyAssignment.add(assignedJob);
		}
		return greedyAssignment;
	}

	/**
	 * Calculates the total value of the greedy assignment based on the benefit
	 * matrix.
	 *
	 * @return The total value of the greedy assignment.
	 */
	public int greedyAssignmentTotalValue() {
		ArrayList<Integer> greedyAssignment = getGreedyAssignment();
		int greedyAssignmentTotalValue = checkValueOfAssignment(greedyAssignment, this.benefitMatrix);
		return greedyAssignmentTotalValue;
	}
}
