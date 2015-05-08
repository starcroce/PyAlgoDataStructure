from collections import deque
import heapq
import sys

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


def DFS_traversal(start_vertex):
    res, visited = [], set()
    DFS_traversal_helper(start_vertex, res, visited)
    return res


def DFS_traversal_helper(start_vertex, res, visited):
    res.append(start_vertex)
    visited.add(start_vertex)
    for adj_vertex in start_vertex.adj_list:
        if not adj_vertex in visited:
            DFS_traversal_helper(adj_vertex, res, visited)


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
    print 'BFS traversal res:', bfs_traversal_res

    dfs_traversal_res = BFS_traversal(my_graph.all_vertex['a'])
    print 'DFS traversal res:',dfs_traversal_res

    for id in range(ord('b'), ord('g')):
        shortest_path = dijkstra_shortest_path(my_graph, 'a', chr(id))
        print 'shortest path from a to ' + chr(id) + ':', shortest_path


if __name__ == '__main__':
    main()
