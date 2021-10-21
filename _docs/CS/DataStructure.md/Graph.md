

---
title: 그래프(Graph)
tags: 
 - Graph
 - DFS
 - BFS
 - MST
 - Dijkstra
 - Floyd
description: 그래프(Graph)
permalink: docs/CS/DataStructure/Graph
---

# Graph


## 최단 경로 알고리즘

1. 한 지점에서 다른 한 지점까지의 최단 경로
2. 한 지점에서 다른 모든 지점까지의 최단 경로 - 다익스트라(dijkstra)
3. 모든 지점에서 다른 모든 지점까지의 최단 경로 - 플로이드(floyd)

## 그래프 탐색

1. 깊이 우선 탐색(DFS, Depth First Search) : 스택, 재귀함수 사용
2. 너비 우선 탐색(BFS, Breath Frist search) : 큐 사용

![DFS_BFS](https://user-images.githubusercontent.com/76420201/124084659-2ff72480-da8a-11eb-8a87-9dfa8920323a.gif)

## 최소 신장 트리

1. Minimum spanning Tree, MST : Kruskal Algorithm, Prim's Algorithm 


## 너비 우선 탐색(BFS)

- 너비 우선 탐색(BFS, Breath Frist search) : 큐 사용
- 간선간의 비용이 같을때 사용

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


## 깊이 우선 탐색(DFS)

- 깊이 우선 탐색(DFS, Depth First Search) : 스택, 재귀함수 사용

### 스택
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


### 재귀
```python

# DFS 2차원 배열 0, 0 -> n, m 까지 가장 큰 경로
max_coin = 0

def Func(coin:list, start_p:tuple, end_p:tuple, total_coin=0):
    global max_coin

    y, x = start_p
    n, m = end_p
    total_coin += coin[y][x]

    if start_p == end_p: # 종점
        max_coin = max_coin if (max_coin > total_coin) else total_coin
    if x < m: # 오른쪽
        Func(coin, (y, x+1), end_p, total_coin)
    if y < n: # 아래
        Func(coin, (y+1, x), end_p, total_coin)
    if x < m and y < n: # 우측대각선
        Func(coin, (y+1, x+1), end_p, total_coin)


def Solution(coin:list):
    answer = 0
    n = len(coin)
    m = len(coin[0])

    Func(coin, (0, 0), (n-1, m-1))

    answer = max_coin
    return answer

coin = [[2, 3, 5, 1, 1], [0, 0, 7, 4, 5], [4, 1, 6, 3, 5], [0, 0, 5, 0, 1]]
print(Solution(coin))
```