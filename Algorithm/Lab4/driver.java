public class driver {
    public static void main(String[] args) {
        // // Creating a directed graph
        // // String[] labels = { "a", "b", "c", "d", "e", "f", "g", "h" };
        // // Graph G = new Graph(labels, false);
        // // G.addEdge("a", "b");
        // // G.addEdge("a", "e");
        // // G.addEdge("a", "f");
        // // G.addEdge("b", "f");
        // // G.addEdge("b", "g");
        // // G.addEdge("c", "d");
        // // G.addEdge("c", "g");
        // // G.addEdge("d", "h");
        // // G.addEdge("e", "f");
        // // G.addEdge("g", "h");

        // // System.out.println("Graph:");
        // // System.out.println(G);

        // // // Running DFS on the directed graph

        // // System.out.println("DFS order traversal of graph:");
        // // G.runDFS(false);

        // // // Running BFS on the directed graph
        // // System.out.println("BFS order traversal of graph:");
        // // G.runBFS(false);

        // // String[] vnames = { "a", "b", "c", "d" };
        // // Graph G = new Graph(vnames, true);

        // // G.addEdge("a", "b");
        // // G.addEdge("a", "d");
        // // G.addEdge("b", "c");
        // // G.addEdge("b", "d");
        // // G.addEdge("c", "d");

        // // Sample graph data
        // String[] vertexLabels = { "a", "b", "c", "d" };
        // Graph G = new Graph(vertexLabels, false);

        // // Adding edges to the graph
        // // G.addEdge("a", "b");
        // // G.addEdge("a", "e");
        // // G.addEdge("a", "f");
        // // G.addEdge("b", "f");
        // // G.addEdge("b", "g");
        // // G.addEdge("c", "d");
        // // G.addEdge("c", "g");
        // // G.addEdge("d", "h");
        // // G.addEdge("e", "f");
        // // G.addEdge("g", "h");

        // // Undirected Connected Graph (Acyclic)
        // // G.addEdge("a", "b");
        // // G.addEdge("a", "d");
        // // G.addEdge("b", "c");
        // // G.addEdge("b", "e");
        // // G.addEdge("c", "e");
        // // G.addEdge("d", "e");
        // // [a, b, c, e, d]
        // // [a, b, d, c, e]

        // // Directed Connected Graph (Acyclic)
        // // G.addEdge("a", "b");
        // // G.addEdge("a", "d");
        // // G.addEdge("b", "c");
        // // G.addEdge("d", "e");
        // // G.addEdge("e", "f");
        // // [a, b, c, d, e, f]
        // // [a, b, d, c, e, f]

        // // Graph with Zero Edges
        // // [a]
        // // [a]

        // // Undirected Connected Graph (Cyclic)
        // // G.addEdge("a", "b");
        // // G.addEdge("a", "d");
        // // G.addEdge("b", "c");
        // // G.addEdge("c", "d");
        // // [a, b, c, d]
        // // [a, b, d, c]

        // // Directed Connected Graph (Cyclic)
        // G.addEdge("a", "b");
        // G.addEdge("a", "d");
        // G.addEdge("b", "c");
        // G.addEdge("c", "d");
        // G.addEdge("d", "a"); // creating a cycle
        // // [a, b, c, d]
        // // [a, b, d, c]

        // // Displaying the adjacency matrix
        // System.out.println("Adjacency Matrix:");
        // System.out.println(G);

        // // Performing DFS
        // System.out.println("DFS order traversal of graph:");
        // G.runDFS(false);

        // // Performing BFS
        // System.out.println("BFS traversal of graph:");
        // G.runBFS(false);

        String[] vnames1 = { "a", "b", "c", "d" };
        Graph G1 = new Graph(vnames1, true);

        G1.addEdge("a", "b");
        G1.addEdge("a", "d");
        G1.addEdge("b", "c");
        G1.addEdge("b", "d");
        G1.addEdge("c", "d");

        System.out.println("Adjacency Matrix:");
        System.out.println(G1);
        System.out.println();
        // Performing DFS
        System.out.println("G1 DFS order traversal of graph:");
        G1.runDFS(false);
        // System.out.println(G.getLastDFSOrder());

        System.out.println();
        // Performing BFS
        System.out.println("G1 BFS traversal of graph:");
        G1.runBFS(false);
        System.out.println(G1.getLastBFSOrder());

        // Sample graph data
        String[] vnames2 = { "a", "b", "c", "d", "e", "f", "g", "h" };
        Graph G2 = new Graph(vnames2, false);

        // Adding edges to the graph
        G2.addEdge("a", "b");
        G2.addEdge("a", "e");
        G2.addEdge("a", "f");
        G2.addEdge("b", "f");
        G2.addEdge("b", "g");
        G2.addEdge("c", "d");
        G2.addEdge("c", "g");
        G2.addEdge("d", "h");
        G2.addEdge("e", "f");
        G2.addEdge("g", "h");

        // Undirected Connected Graph (Acyclic)
        G2.addEdge("a", "b");
        G2.addEdge("a", "d");
        G2.addEdge("b", "c");
        G2.addEdge("b", "e");
        G2.addEdge("c", "e");
        G2.addEdge("d", "e");
        // [a, b, c, e, d]
        // [a, b, d, c, e]

        // Directed Connected Graph (Acyclic)
        G2.addEdge("a", "b");
        G2.addEdge("a", "d");
        G2.addEdge("b", "c");
        G2.addEdge("d", "e");
        G2.addEdge("e", "f");
        // [a, b, c, d, e, f]
        // [a, b, d, c, e, f]

        System.out.println("Adjacency Matrix:");
        System.out.println(G2);
        System.out.println();

        // Performing DFS
        System.out.println("G2 DFS order traversal of graph:");
        G2.runDFS(false);
        // System.out.println(G.getLastDFSOrder());

        System.out.println();
        // Performing BFS
        System.out.println("G2 BFS traversal of graph:");
        G2.runBFS(false);
        System.out.println(G2.getLastBFSOrder());

        // Graph with Zero Edges
        String[] vnames3 = { "a" };
        Graph G3 = new Graph(vnames3, false);
        // [a]
        // [a]

        System.out.println("Adjacency Matrix:");
        System.out.println(G3);
        System.out.println();

        // Performing DFS
        System.out.println("G3 DFS order traversal of graph:");
        G3.runDFS(false);
        // System.out.println(G3.getLastDFSOrder());

        System.out.println();
        // Performing BFS
        System.out.println("G3 BFS traversal of graph:");
        G3.runBFS(false);
        System.out.println(G3.getLastBFSOrder());

        // Graph with Zero Edges
        String[] vnames4 = { "a", "b", "c", "d" };
        Graph G4 = new Graph(vnames4, false);
        // Undirected Connected Graph (Cyclic)
        G4.addEdge("a", "b");
        G4.addEdge("a", "d");
        G4.addEdge("b", "c");
        G4.addEdge("c", "d");
        // [a, b, c, d]
        // [a, b, d, c]

        System.out.println("Adjacency Matrix:");
        System.out.println(G4);
        System.out.println();

        // Performing DFS
        System.out.println("G4 DFS order traversal of graph:");
        G4.runDFS(false);
        // System.out.println(G.getLastDFSOrder());

        System.out.println();
        // Performing BFS
        System.out.println("G4 BFS traversal of graph:");
        G4.runBFS(false);
        System.out.println(G4.getLastBFSOrder());

        // Directed Connected Graph (Cyclic)
        String[] vnames5 = { "a", "b", "c", "d" };
        Graph G5 = new Graph(vnames5, false);
        G5.addEdge("a", "b");
        G5.addEdge("a", "d");
        G5.addEdge("b", "c");
        G5.addEdge("c", "d");
        G5.addEdge("d", "a"); // creating a cycle
        // [a, b, c, d]
        // [a, b, d, c]

        System.out.println("Adjacency Matrix:");
        System.out.println(G5);
        System.out.println();

        // Performing DFS
        System.out.println("G5 DFS order traversal of graph:");
        G5.runDFS(false);
        // System.out.println(G5.getLastDFSOrder());

        System.out.println();
        // Performing BFS
        System.out.println("G5 BFS traversal of graph:");
        G5.runBFS(false);
        System.out.println(G5.getLastBFSOrder());

    }
}
