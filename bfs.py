from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 4, 5],
    4: [1, 2, 3, 5],
    5: [3, 4]
}

start_node = 0
print("BFS Traversal:", bfs_traversal(graph, start_node))
