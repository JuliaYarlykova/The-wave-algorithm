from collections import deque


def algorithm(graph, start_node, end_node):
    def bfs(graph, start, end):
        queue = deque()
        queue.append((start, [start]))

        while queue:
            (node, path) = queue.popleft()
            if node == end:
                return path
            for neighbor in range(len(graph[node-1])):
                if graph[node-1][neighbor] == 1 and neighbor+1 not in path:
                    queue.append((neighbor+1, path + [neighbor+1]))

    shortest_path = bfs(graph, start_node, end_node)

    return shortest_path

def algorithm2(graph, start_node, end_node, list_weight):
    def bfs(graph, start, end, list_weight):
        queue = deque()
        queue.append((start, [start]))

        while queue:
            n_b = 0
            (node, path) = queue.popleft()
            minimum = 1000
            if node == end:
                return path
            for neighbor in range(len(graph[node-1])):
                if graph[node-1][neighbor] == 1 and neighbor+1 not in path:
                    if minimum > (list_weight[str(node) + str(neighbor+1)] or list_weight[str(neighbor+1) + str(node)]):
                        minimum = list_weight[str(node) + str(neighbor+1)]
                        n_b = neighbor
                        print(n_b, minimum)
            print(n_b)
            queue.append((n_b+1, path + [n_b+1]))

    shortest_path = bfs(graph, start_node, end_node, list_weight)

    return shortest_path

mat = [
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

list_w = {
    '12':3,
    '13':10,
    '23':1
}

print(algorithm(mat,1,3))
