import heapq

def orangeRotting(grid):
    rotted = set()
    seen = set()
    fresh = set()
    oranges = set()
    pq = []
    graph = dict()
    row = len(grid[0])
    column = len(grid)
    #create graph
    graph["source"] = []

    for i in range(column):
        for j in range(row):
            if grid[i][j] > 0:
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotted.add((i,j))
                    graph["source"].append((i,j))
                oranges.add((i,j))
                graph[(i,j)] = []
                if j > 0:
                    if grid[i][j-1] > 0:
                        graph[(i,j)].append((i,j-1))
                if i > 0:
                    if grid[i-1][j] > 0:
                        graph[(i,j)].append((i-1,j))
                if j < row-1:
                    if grid[i][j+1] > 0:
                        graph[(i,j)].append((i,j+1))
                if i < column-1:
                    if grid[i+1][j] > 0:
                        graph[(i,j)].append((i+1,j))


    if len(fresh) == 0:
        return 0
    if len(rotted)== 0 and len(fresh) >0:
        return -1

    pq.extend(graph["source"])
    seen.add("source")
    prev = "source"
    count = -1
    while len(pq) > 0:
        node = pq.pop(0)
        if node not in seen:











    return graph


print(orangeRotting([[2,1,1],[1,1,0],[0,1,1]]))
