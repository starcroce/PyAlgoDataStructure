from collections import deque

import  MyUndirectedGraph


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


def main():
    my_graph = MyUndirectedGraph.Graph()
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
    print bfs_traversal_res


if __name__ == '__main__':
    main()
