from collections import deque
import heapq
import sys

import  MyGraph


def BFS_traversal(start_vertex):
    res, queue, visited = [], deque([start_vertex]), set()
    visited.add(start_vertex)
    while len(queue) > 0:
        tmp_vertex = queue.popleft()
        res.append(tmp_vertex.id)
        for adj_vertex in tmp_vertex.adj_list:
            if not adj_vertex in visited:
                queue.append(adj_vertex)
                visited.add(adj_vertex)
    return res


def DFS_traversal(start_vertex):

    def DFS_traversal_helper(start_vertex):
        res.append(start_vertex)
        visited.add(start_vertex)
        for adj_vertex in start_vertex.adj_list:
            if not adj_vertex in visited:
                DFS_traversal_helper(adj_vertex)

    res, visited = [], set()
    DFS_traversal_helper(start_vertex)
    return res


def dijkstra_shortest_path(graph, start_id, end_id):
    distance, prev_vertex, unvisited_queue, visited = {}, {}, [], set()
    distance[start_id], prev_vertex[start_id] = 0, None

    for v_id in graph.all_vertex:
        if v_id != start_id:
            distance[v_id] = sys.maxint
            prev_vertex[v_id] = None
        unvisited_queue.append((distance[v_id], v_id))
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) > 0:
        curr_vertex = graph.all_vertex[heapq.heappop(unvisited_queue)[1]]
        visited.add(curr_vertex.id)
        for adj_vertex in curr_vertex.adj_list:
            alt_dist = distance[curr_vertex.id] + curr_vertex.adj_list[adj_vertex]
            if alt_dist < distance[adj_vertex.id]:
                distance[adj_vertex.id] = alt_dist
                prev_vertex[adj_vertex.id] = curr_vertex.id

        unvisited_queue = [(distance[v_id], v_id) for v_id in graph.all_vertex if not v_id in visited]
        heapq.heapify(unvisited_queue)

    res, dst_id = [], end_id
    while dst_id:
        res.append(dst_id)
        dst_id = prev_vertex[dst_id]
    return res[::-1]


def kruskal_minimum_spanning_tree(graph, start_id):
    parent, rank = {}, {}

    def make_set(vertex):
        parent[vertex] = vertex
        rank[vertex] = 0

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(vertex_1, vertex_2):
        root_1, root_2 = find(vertex_1), find(vertex_2)
        if root_1 != root_2:
            if rank[root_1] > rank[root_2]:
                parent[root_2] = root_1
            else:
                parent[root_1] = root_2
                if rank[root_1] == rank[root_2]:
                    rank[root_2] += 1

    all_edges = set()
    for vertex in graph.all_vertex:
        make_set(vertex)
        vertex = graph.all_vertex[vertex]
        neighbors = vertex.adj_list
        for neighbor in neighbors:
            edge = (neighbors[neighbor], tuple(sorted([vertex.id, neighbor.id])))
            all_edges.add(edge)
    all_edges = sorted(list(all_edges))

    minimum_spanning_tree = []
    for edge in all_edges:
        length, vertex_1, vertex_2 = edge[0], edge[1][0], edge[1][1]
        if find(vertex_1) != find(vertex_2):
            union(vertex_1, vertex_2)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree


def main():
    """
          b---d
         /|  /|\
        a | / | f
         \|/  |/
          c---e
        ab = 4, ac = 2, bc = 1,
        bd = 4, cd = 8, ce = 10,
        de = 2, df = 6, ef = 3
    """
    my_graph = MyGraph.Graph()
    for i in range(ord('a'), ord('g')):
        my_graph.add_vertex(chr(i))

    my_graph.add_edge('a', 'b', 4)
    my_graph.add_edge('a', 'c', 2)
    my_graph.add_edge('c', 'b', 1)

    my_graph.add_edge('d', 'b', 5)
    my_graph.add_edge('c', 'd', 8)
    my_graph.add_edge('c', 'e', 10)

    my_graph.add_edge('d', 'e', 2)
    my_graph.add_edge('d', 'f', 6)
    my_graph.add_edge('e', 'f', 3)

    bfs_traversal_res = BFS_traversal(my_graph.all_vertex['a'])
    print 'BFS traversal res:', bfs_traversal_res

    dfs_traversal_res = BFS_traversal(my_graph.all_vertex['a'])
    print 'DFS traversal res:',dfs_traversal_res

    for id in range(ord('b'), ord('g')):
        shortest_path = dijkstra_shortest_path(my_graph, 'a', chr(id))
        print 'shortest path from a to ' + chr(id) + ':', shortest_path

    kmst = kruskal_minimum_spanning_tree(my_graph, 'a')
    print 'kruskal minimum spanning tree:', kmst


if __name__ == '__main__':
    main()
