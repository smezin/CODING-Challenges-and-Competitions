from queue import deque
from typing import List

def allPathsSourceTarget(start: int, end: int, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        
        def backtrack(node, path):
            if node == end:
                paths.append(list(path))
                return 
            for nextNode in graph[node]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
                
        path = deque([start])
        backtrack(start, path)
        return paths

g = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPathsSourceTarget(1, 4, g))