import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class driver {
    public static void main(String[] args) {
        // File paths for input data files
        String filePath1 = "37names.txt";

        // Size of the hash table
        int tableSize = 3700;

        // Create a HashSimulator object
        HashSimulator hashSimulator = new HashSimulator();

        try {
            // Read keys from file 1
            String[] keys = readKeysFromFile(filePath1);
            // Run the hash simulation for keys from file 1
            int[] results1 = hashSimulator.runHashSimulation(keys, tableSize);

            // Display the results for file 1
            displayResults(results1);

        } catch (IOException e) {
            System.err.println("Error reading input files: " + e.getMessage());
        }
    }

    // Method to read keys from a file
    private static String[] readKeysFromFile(String filePath) throws IOException {
        List<String> keys = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                keys.add(line);
            }
        }
        return keys.toArray(new String[0]);
    }

    // Method to display the results
    private static void displayResults(int[] results) {
        System.out.println("H1 Collisions: " + results[0]);
        System.out.println("H1 Probes: " + results[1]);
        System.out.println("H2 Collisions: " + results[2]);
        System.out.println("H2 Probes: " + results[3]);
        System.out.println("H3 Collisions: " + results[4]);
        System.out.println("H3 Probes: " + results[5]);
    }

}
