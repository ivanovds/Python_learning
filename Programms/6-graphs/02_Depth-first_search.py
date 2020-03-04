def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
 
graph = {'0': set(['1', '5']),
         '1': set(['2', '4']),
         '2': set(['3']),
         '3': set(['1']),
         '4': set([]),
         '5': set(['6']),
         '6': set(['7', '8']),
         '7': set([]),
         '8': set([]),
         }
 
dfs(graph, '0')