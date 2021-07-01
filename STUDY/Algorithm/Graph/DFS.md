
# DFS

- 깊이 우선 탐색(DFS, Depth First Search) : 스택, 재귀함수 사용

```python
def DFS(graph, root):
    """
    graph = {
        '1': ['2', '3', '4'], 
        '2': ['1', '4'], 
        '3': ['1', '4'], 
        '4': ['1', '2', '3']
        }
    """
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited) # 1 2 4 3
```