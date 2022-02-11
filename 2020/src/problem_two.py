from functools import reduce


M = int(input()) # rows
N = int(input()) # cols
grid = [list(map(int, input().split())) for _ in range(M)]

def main():
    graph = create_graph()
    
    visited = bfs(graph)

    if len(visited) == 1:
        print('no')
    elif grid[M-1][N-1] in visited:
        print('yes')
    else:
        print('no')
   
def create_graph():
    graph = {}
   
    for r in range(M):
        for c in range(N):
            curr_num = grid[r][c]
            graph[curr_num] = factors(curr_num)
           
    return graph

def factors(n):    
    return list(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
       
def bfs(graph):
    visited = []
    queue = []
   
    visited.append(grid[0][0])
    queue.append(grid[0][0])
   
    while queue:
        s = queue.pop(0)

        for x in graph[s]:
            row = s//x
            col = x
           
            if (row > M or col > N): continue
            if grid[row-1][col-1] in visited: continue

            queue.append(grid[row-1][col-1])
            visited.append(grid[row-1][col-1])
           
            if grid[row-1][col-1] == grid[M-1][N-1]:
                queue = []
                break

    return visited
   


main()

# scored 11/15