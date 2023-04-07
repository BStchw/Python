from graph import Graph

graph = Graph()

graph.read_csvgraph("graph.csv")

print("Graf początkowy:")
graph.print_graph()

graph2 = graph.floyd_warshall()
print("Graf z najkrótszymi odległościami między wierzchołkami:")
graph2.print_graph()