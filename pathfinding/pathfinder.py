import heapq
from util.point_utils import distance_2d, neighbours_2d_diagonal

def get_path(start_node, end_node, get_neighbours, get_cost, is_end_node = None):
    visited = set()
    visited.add(start_node)
    first_path = [start_node]
    queue = [(get_cost(first_path, end_node), first_path)]
    heapq.heapify(queue)

    while len(queue) > 0:
        priority, path = heapq.heappop(queue)
        
        if (is_end_node and is_end_node(path[-1])) or path[-1] == end_node:
            return path
        
        for node in get_neighbours(path[-1]):
            if node in visited:
                continue

            visited.add(node)
            new_path = path.copy()
            new_path.append(node)
            heapq.heappush(queue, (get_cost(new_path, end_node), new_path))

def get_web(nodes, get_neighbours, get_cost):
    web = [[None for node in nodes] for other in nodes]

    for i in range(len(nodes)):
        for j in range(len(nodes) - i):
            n1 = nodes[i]
            n2 = nodes[i + j]

            print(f'Finding path between nodes {i} and {i + j}')
            path = get_path(n1, n2, get_neighbours, get_cost)

            web[i][i + j] = path
            web[i + j][i] = path[::-1] if path is not None else path
    
    return web