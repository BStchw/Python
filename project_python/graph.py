import csv

class Graph:
    def __init__(self):
        self.graph_list = {}

    def add_node(self, node):
        """Wstawia wierzchołek do grafu."""
        if node not in self.graph_list:
            self.graph_list[node] = []

    def add_edge_directed(self, source, target, weight):
        """Dodaje krawędź do grafu skierowanego."""
        self.add_node(source)
        self.add_node(target)
        if source == target:
            raise ValueError("pętle są zabronione")
        if (target, weight) not in self.graph_list[source]:
            self.graph_list[source].append((target, weight))

    def list_nodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self.graph_list.keys()

    def list_edges(self):
        """Zwraca listę krawędzi (3-krotek) grafu skierowanego ważonego."""
        L = []
        for source in self.graph_list:
            for (target, weight) in self.graph_list[source]:
                L.append((source, target, weight))
        return L

    def print_graph(self):
        """Wypisuje postać grafu skierowanego ważonego na ekranie."""
        L = []
        for source in self.graph_list:
            L.append("{} : ".format(source))
            for (target, weight) in self.graph_list[source]:
                L.append("{}({}) ".format(target, weight))
            L.append("\n")
        print("".join(L))

    def floyd_warshall(self):
        '''distance, tworze macierz odleglosci dla grafu, poczatkowo macierz jest wypelniona wartosciami INF'''
        distance = [[float("inf")] * len(self.list_nodes()) for _ in range(len(self.list_nodes()))]

        '''Aktualizuje wartosci odleglosci wierzcholka do jego samego, odleglosc = 0'''
        for i in range(0, len(self.list_nodes())):
            distance[i][i] = 0

        '''Aktualizuje wartosci odleglosci z bezposrednich krawedzi'''
        for edge in self.list_edges():
            source_index = list(self.list_nodes()).index(edge[0])
            target_index = list(self.list_nodes()).index(edge[1])
            distance[source_index][target_index] = edge[2]

        '''Algorytm:'''
        for k in range(len(self.list_nodes())):
            for i in range(len(self.list_nodes())):
                for j in range(len(self.list_nodes())):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        for i in range(len(self.list_nodes())):
            if (distance[i][i] < 0):
                raise ValueError("Graf ma ujemne cykle")

        '''Zwracanie nowego grafu'''
        newgraph = Graph()
        for element1 in self.list_nodes():
            for element2 in self.list_nodes():
                source_index = list(self.list_nodes()).index(element1)
                target_index = list(self.list_nodes()).index(element2)
                if ((distance[source_index][target_index] != float("inf")) and (source_index != target_index)):
                    newgraph.add_edge_directed(element1, element2, distance[source_index][target_index])
        return newgraph

    def read_csvgraph(self, csvfile):
        with open(csvfile, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                a, b, s = row
                c = int(s)
                self.add_edge_directed(a, b, c)
        return self
