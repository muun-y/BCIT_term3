import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Represents a graph data structure using an adjacency matrix.
 * An adjacency matrix is a 2D array where the presence of an edge between
 * vertices
 * is indicated by a non-zero value at the corresponding matrix entry.
 * This class supports both directed and undirected graphs.
 * 
 * @author Mun Young Cho (A01330048) Set C
 */
public class Graph {
    private String[] vertexLabels;
    private boolean isDirected;
    private int[][] adjMatrix;
    private boolean[] visited;
    private ArrayList<String> lastDFSOrder;
    private ArrayList<String> lastDFSDeadEndOrder;
    private ArrayList<String> lastBFSOrder;

    /**
     * Initializes a new Graph instance with the given vertex labels and
     * directionality.
     *
     * @param vertexLabels The array of vertex labels.
     * @param isDirected   True if the graph is directed, false otherwise.
     */
    public Graph(String[] vertexLabels, boolean isDirected) {
        this.vertexLabels = vertexLabels;
        this.isDirected = isDirected;
        this.adjMatrix = new int[vertexLabels.length][vertexLabels.length];
        this.visited = new boolean[vertexLabels.length];
        this.lastDFSOrder = new ArrayList<>();
        this.lastDFSDeadEndOrder = new ArrayList<>();
        this.lastBFSOrder = new ArrayList<>();
    }

    /**
     * Checks if the graph is directed.
     *
     * @return True if the graph is directed, false otherwise.
     */
    public boolean isDirected() {
        return isDirected;
    }

    /**
     * Adds an edge between two vertices in the graph.
     *
     * @param start The label of the starting vertex.
     * @param end   The label of the ending vertex.
     */
    public void addEdge(String start, String end) {
        int startIndex = getIndex(start);
        int endIndex = getIndex(end);
        adjMatrix[startIndex][endIndex] = 1;
        if (!isDirected) {
            adjMatrix[endIndex][startIndex] = 1;
        }
    }

    /**
     * Gets the number of vertices in the graph.
     *
     * @return The number of vertices.
     */
    public int size() {
        return vertexLabels.length;
    }

    /**
     * Gets the label of the vertex at the specified index.
     *
     * @param v The index of the vertex.
     * @return The label of the vertex.
     */
    public String getLabel(int v) {
        return vertexLabels[v];
    }

    /**
     * Returns a string representation of the graph's adjacency matrix.
     * The matrix representation shows the connections between vertices.
     *
     * @return A string representation of the adjacency matrix.
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int[] row : adjMatrix) {
            for (int val : row) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
        }
        return sb.toString().trim();
    }

    /**
     * Runs a depth-first search (DFS) traversal on the graph.
     *
     * @param quiet True to suppress output, false otherwise.
     */
    public void runDFS(boolean quiet) {
        lastDFSOrder.clear();
        lastDFSDeadEndOrder.clear();
        visited = new boolean[vertexLabels.length];
        for (int i = 0; i < vertexLabels.length; i++) {
            if (!visited[i]) {
                dfs(i, quiet);
            }
        }
    }

    /**
     * Runs a depth-first search (DFS) traversal starting from the specified vertex.
     *
     * @param v     The label of the starting vertex.
     * @param quiet True to suppress output, false otherwise.
     */
    public void runDFS(String v, boolean quiet) {
        int index = getIndex(v);
        lastDFSOrder.clear();
        lastDFSDeadEndOrder.clear();
        visited = new boolean[vertexLabels.length];
        dfs(index, quiet);
    }

    /**
     * Performs a depth-first search (DFS) traversal starting from the given vertex.
     * Visits vertices in a recursive manner, marking them as visited and adding
     * them to the traversal order.
     *
     * @param v     The index of the vertex to start the DFS traversal from.
     * @param quiet True to suppress output during traversal, false to print visited
     *              vertices.
     */
    private void dfs(int v, boolean quiet) {
        visited[v] = true;
        lastDFSOrder.add(vertexLabels[v]);
        if (!quiet) {
            System.out.println("Visiting vertex " + vertexLabels[v]);
        }
        for (int i = 0; i < vertexLabels.length; i++) {
            if (adjMatrix[v][i] == 1 && !visited[i]) {
                dfs(i, quiet);
            }
        }
        if (!quiet) {
            lastDFSDeadEndOrder.add(vertexLabels[v]);
        }
    }

    /**
     * Runs a breadth-first search (BFS) traversal on the graph.
     *
     * @param quiet True to suppress output, false otherwise.
     */
    public void runBFS(boolean quiet) {
        lastBFSOrder.clear();
        visited = new boolean[vertexLabels.length];
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < vertexLabels.length; i++) {
            if (!visited[i]) {
                queue.offer(i);
                visited[i] = true;
                lastBFSOrder.add(vertexLabels[i]);
                while (!queue.isEmpty()) {
                    int current = queue.poll();
                    for (int j = 0; j < vertexLabels.length; j++) {
                        if (adjMatrix[current][j] == 1 && !visited[j]) {
                            queue.offer(j);
                            visited[j] = true;
                            lastBFSOrder.add(vertexLabels[j]);
                        }
                    }
                    if (!quiet) {
                        System.out.println("Visiting vertex " + vertexLabels[current]);
                    }
                }
            }
        }
    }

    /**
     * Runs a breadth-first search (BFS) traversal starting from the specified
     * vertex.
     *
     * @param v     The label of the starting vertex.
     * @param quiet True to suppress output, false otherwise.
     */
    public void runBFS(String v, boolean quiet) {
        int index = getIndex(v);
        lastBFSOrder.clear();
        visited = new boolean[vertexLabels.length];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(index);
        visited[index] = true;
        lastBFSOrder.add(vertexLabels[index]);
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int j = 0; j < vertexLabels.length; j++) {
                if (adjMatrix[current][j] == 1 && !visited[j]) {
                    queue.offer(j);
                    visited[j] = true;
                    lastBFSOrder.add(vertexLabels[j]);
                }
            }
        }
    }

    /**
     * Gets the last depth-first search (DFS) traversal order.
     *
     * @return The list of vertices in DFS order.
     */
    public ArrayList<String> getLastDFSOrder() {
        return lastDFSOrder;
    }

    /**
     * Gets the last dead-end depth-first search (DFS) traversal order.
     *
     * @return The list of vertices in dead-end DFS order.
     */
    public ArrayList<String> getLastDFSDeadEndOrder() {
        return lastDFSDeadEndOrder;
    }

    /**
     * Gets the last breadth-first search (BFS) traversal order.
     *
     * @return The list of vertices in BFS order.
     */
    public ArrayList<String> getLastBFSOrder() {
        return lastBFSOrder;
    }

    /**
     * Gets the index of a vertex label in the vertexLabels array.
     *
     * @param label The label of the vertex.
     * @return The index of the vertex label, or -1 if not found.
     */
    private int getIndex(String label) {
        for (int i = 0; i < vertexLabels.length; i++) {
            if (vertexLabels[i].equals(label)) {
                return i;
            }
        }
        return -1;
    }
}
