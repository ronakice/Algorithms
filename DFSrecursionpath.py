#depth first search with path
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D','E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()} 
t=[]
def dfs_paths(graph, start, goal,path=None):
    if path is None:
        path = [start]
    if start == goal:
        t.append(path)
    for next in graph[start] - set(path):
        dfs_paths(graph, next, goal, path + [next])
dfs_paths(graph, 'A', 'D',None)
print(t)