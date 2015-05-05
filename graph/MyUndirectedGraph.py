class Vertex:

    def __init__(self, id):
        self.id = id
        self.adj_list = {}


class Graph:

    def __init__(self):
        self.all_vertex = {}

    def add_vertex(self, id):
        new_vertex = Vertex(id)
        self.all_vertex[id] = new_vertex

    def add_edge(self, id_1, id_2, edge):
        vertex_1, vertex_2 = self.all_vertex[id_1], self.all_vertex[id_2]
        vertex_1.adj_list[self.all_vertex[id_2]] = edge
        vertex_2.adj_list[self.all_vertex[id_1]] = edge

    def remove_edge(self, id_1, id_2):
        vertex_1, vertex_2 = self.all_vertex[id_1], self.all_vertex[id_2]
        del vertex_1.adj_list[self.all_vertex[id_2]]
        del vertex_2.adj_list[self.all_vertex[id_1]]
