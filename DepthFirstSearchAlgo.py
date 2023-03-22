# This is the algorithm for a Depth first search (DFS)
def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        
        # First of all, we add the current node into our visited set
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)

if __name__ == "__main__":
    graph ={
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
    
    # set() is like an array or array where it stores multiple elements. 
    # However it differes where if the same element comes in, it is automatically trashed
    visited = set()
    
    DFS(visited, graph, 'A')
    