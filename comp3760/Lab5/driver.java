import java.io.FileNotFoundException;

public class driver {
    public static void main(String[] args) throws FileNotFoundException {
        JobAssignmentFinder finder = new JobAssignmentFinder();

        // Read data from file (assuming filename is passed as command line argument)
        if (args.length == 0) {
            System.out.println("Usage: java Driver <filename>");
            return;
        }
        String filename = args[0];
        finder.readDataFile(filename);

        // Test getMaxAssignment and getMaxAssignmentTotalValue methods
        // System.out.println("Max Assignment: " + finder.getMaxAssignment());
        // System.out.println("Total value of max assignment: " +
        // finder.getMaxAssignmentTotalValue());

        // Test getGreedyAssignment and greedyAssignmentTotalValue methods
        System.out.println("Greedy Assignment: " + finder.getGreedyAssignment());
        System.out.println("Total value of greedy assignment: " + finder.greedyAssignmentTotalValue());
    }
}
