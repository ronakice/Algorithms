#breadth first search with path
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D','E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()} 
t=[]

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print "Visiting: " + str(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
    
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                t.append(path + [next])
            else:
                queue.append((next, path + [next]))
                
bfs_paths(graph,'A','C')
print(t) #first t will give the shortest path