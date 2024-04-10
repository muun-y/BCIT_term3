/**
 * This class simulates the hash function and stores the results.
 * 
 * The HashSimulator class provides methods to simulate the insertion of items
 * into a hash table
 * using various hash functions and store the results of the simulations. It
 * supports three hash
 * functions: H1, H2, and H3, each of which generates hash values based on
 * different algorithms.
 * 
 * The simulations calculate the number of collisions and probes that occur when
 * inserting keys
 * into the hash table. Collisions happen when two keys are hashed to the same
 * index in the hash
 * table, while probes occur when finding an empty slot after a collision.
 *
 */
public class HashSimulator {

    /**
     * Runs the hash simulation for a given list of keys and hash table size.
     * 
     * @param keys      An array of strings representing the keys to be hashed.
     * @param tableSize The size of the hash table to be used.
     * @return An array of integers containing the results of the hash simulations:
     *         - results[0] is the number of collisions that occur when hashing with
     *         H1().
     *         - results[1] is the number of probes that occur when hashing with
     *         H1().
     *         - results[2] is the number of collisions that occur when hashing with
     *         H2().
     *         - results[3] is the number of probes that occur when hashing with
     *         H2().
     *         - results[4] is the number of collisions that occur when hashing with
     *         H3().
     *         - results[5] is the number of probes that occur when hashing with
     *         H3().
     */
    public int[] runHashSimulation(String[] keys, int tableSize) {
        int[] results = new int[6];

        simulateHash(keys, tableSize, results, 0);

        simulateHash(keys, tableSize, results, 2);

        simulateHash(keys, tableSize, results, 4);

        return results;
    }

    /**
     * Simulates the hash function for the given keys and stores the results.
     * 
     * @param keys       An array of strings representing the keys to be hashed.
     * @param tableSize  The size of the hash table to be used.
     * @param results    An array of integers to store the simulation results.
     * @param startIndex The index in the results array where the simulation results
     *                   should be stored.
     */
    private void simulateHash(String[] keys, int tableSize, int[] results, int startIndex) {
        int collisionCount = 0;
        int probeCount = 0;
        String[] hashTable = new String[tableSize];

        for (String key : keys) {
            int hashValue = startIndex == 0 ? H1(key, tableSize)
                    : (startIndex == 2 ? H2(key, tableSize) : H3(key, tableSize));
            // Check for collision
            if (hashTable[hashValue] != null) {
                collisionCount++;
                // Probe for an empty slot
                int probeIndex = (hashValue + 1) % tableSize;
                while (hashTable[probeIndex] != null) {
                    probeCount++;
                    probeIndex = (probeIndex + 1) % tableSize;
                }
                // Place the key in the first available empty slot (probeIndex)
                hashTable[probeIndex] = key;
            } else {
                // No collision, place the key in the designated slot
                hashTable[hashValue] = key;
            }
        }

        results[startIndex] = collisionCount;
        results[startIndex + 1] = probeCount + collisionCount;
    }

    /**
     * Hash function H1.
     * 
     * This hash function sums up the alphabetical positions of the characters in
     * the input string,
     * and then takes the modulo of the sum with the hash table size.
     * 
     * @param name   The key to be hashed.
     * @param HTsize The size of the hash table.
     * @return The hash value of the key.
     */
    public int H1(String name, int HTsize) {
        int sum = 0;
        for (char c : name.toCharArray()) {
            sum += (c - 'A' + 1);
        }
        return sum % HTsize;
    }

    /**
     * Hash function H2.
     * 
     * This hash function calculates the hash value based on the position and
     * character value of
     * each character in the input string.
     * 
     * @param name   The key to be hashed.
     * @param HTsize The size of the hash table.
     * @return The hash value of the key.
     */
    public int H2(String name, int HTsize) {
        long sum = 0;
        for (int i = 0; i < name.length(); i++) {
            sum += (name.charAt(i) - 'A' + 1) * Math.pow(26, i);
        }
        return (int) (sum % HTsize);
    }

    /**
     * Hash function H3.
     * 
     * This hash function iterates over each character in the input string and
     * calculates the hash value based on a prime number (31) and the ASCII value of
     * the character.
     * source of the function: stackoverflow.com
     * 
     * @param name   The key to be hashed.
     * @param HTsize The size of the hash table.
     * @return The hash value of the key.
     */
    public int H3(String name, int HTsize) {
        int hash = 0;
        for (int i = 0; i < name.length(); i++) {
            hash = (31 * hash + name.charAt(i)) % HTsize;
        }
        return hash;
    }
}
