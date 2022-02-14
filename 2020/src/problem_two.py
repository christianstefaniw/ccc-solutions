from collections import defaultdict

M = int(input()) # rows
N = int(input()) # cols
grid = [list(map(int, input().split())) for _ in range(M)]

def main():
    graph = init_graph()
    path = bfs(grid[0][0], graph)
    print(can_escape(path))

def init_graph():
    graph = defaultdict(list)
    for row_index in range(M):
        for col_index in range(N):
            valid_val = (row_index + 1) * (col_index + 1)
            graph[valid_val].append([row_index, col_index])

    return graph

def bfs(node, graph):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop()
        for neighbour in graph[s]:
            key_val = grid[neighbour[0]][neighbour[1]]
            if key_val not in visited:
                visited.append(key_val)
                queue.append(key_val)

    return visited

def can_escape(path):
    if len(path) == 1:
        return 'no'

    final_dest = grid[M-1][N-1]
    for step in path:
        if step == final_dest:
            return 'yes'
    return 'no'

main()

'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9
'''