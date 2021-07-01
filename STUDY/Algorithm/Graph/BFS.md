
# 너비 우선 탐색(BFS)

- 너비 우선 탐색(BFS, Breath Frist search) : 큐 사용

```python
from collections import deque

def BFS(graph, root):
    """
    graph = {
        '1': ['2', '3', '4'], 
        '2': ['1', '4'], 
        '3': ['1', '4'], 
        '4': ['1', '2', '3']
        }
    """
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return ' '.join(str(i) for i in visited) # 1 2 3 4
```