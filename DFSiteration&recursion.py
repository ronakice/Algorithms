#depth first search
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D','E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}
def dfs(graph, start):
    visited=set()
    stack=[start]
    while(stack):
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited
print (list(dfs(graph,'B')))
#dfs recursion
def dfsr(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    for next in graph[start]-visited:
        dfsr(graph,next,visited)
    return visited
print (list(dfs(graph,'G')))     


   