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

- 최단 경로 알고리즘

1. 한 지점에서 다른 한 지점까지의 최단 경로
2. 한 지점에서 다른 모든 지점까지의 최단 경로 - 다익스트라(dijkstra)
3. 모든 지점에서 다른 모든 지점까지의 최단 경로 - 플로이드(floyd)

- 그래프 탐색

1. 깊이 우선 탐색(DFS, Depth First Search) : 스택, 재귀함수 사용
2. 너비 우선 탐색(BFS, Breath Frist search) : 큐 사용

![DFS_BFS](https://user-images.githubusercontent.com/76420201/124084659-2ff72480-da8a-11eb-8a87-9dfa8920323a.gif)

- 최소 신장 트리

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

**스택**
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


**재귀**
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



## 최단 경로 알고리즘(Dijkstra)

- 다익스트라(Dijkstra Algorithm)
- 다익스트라 알고리즘은 greedy 알고리즘이며 단방향, 양방향(사이클) 모두 사용 가능
- 너비 우선 탐색(BFS) 방식과 유사

### 다익스트라 알고리즘

- 우선순위 큐로 구현
- 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산
- 더 긴 거리로 계산된 루트에 대해서는 계산을 스킵

```python
import heapq

def dijkstra(graph, start):
    '''
    graph = {
        'A' : {'B': 8, 'C': 1, 'D': 2},
        'B' : {},
        'C' : {'B': 5, 'D': 2},
        'D' : {'E': 3, 'F': 5},
        'E' : {'F': 1},
        'F' : {'A': 5}
    }
    '''

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start]) # (거리, 노드) 첫번째 값으로 정렬 됨(거리로 정렬이 됨)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances # {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
```


## 최단 경로 알고리즘(Floyd Warshall)

- 모든 지점에서 다른 모든 지점까지의 최단 경로
- 동적 프로그래밍(Dynamic programming)기법
- 점화식 :
$$ \begin{aligned} & D_k(i,j) = min(D_{k-1}(i, j), D_{k-1}(i,k) + D_{k-1}(k,j)) \end{aligned}$$

```python
def Floyd_warshall(n, data):
    dist = [[float('inf')] * n for _ in range(n)]

    for i, j, edge in data:
        dist[i-1][j-1] = edge
        
    for k in range(n):
        dist[k][k] = 0
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]: # 시간 절약 1/2
                    dist[i][j] = dist[i][k] + dist[k][j]
                # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

n = 4
data = [[1,3,-2],[2,1,4],[2,3,3],[3,4,2],[4,2,-1]]
print(Floyd_warshall(n, data)) # [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
```



## 최소 신장 트리(Kruskal)

- 최소 신장 트리 (MST, Minimum Spanning Tree)
- 간선의 가중치 합이 최소인 Spanning Tree
- **Greedy Algorithm(탐욕법)**을 기초로 하고 있음


- 구현
1. 모든 정점을 독립적인 집합으로 만든다.
2. 모든 간선의 비용을 정렬하고 비용이 작은 간선부터 정점을 비교
3. 두 정점의 최상위 정점(루트)을 확인하고 서로 다를 경우 연결(사이클이 생기지 않도록 하기 위함) 

```python
nodes = []

def find(u):
    if u != nodes[u]:
        nodes[u] = find(nodes[u])

    return nodes[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    nodes[root2] = root1

# kruskal
def solution(n, cost):

    global nodes
    answer = 0
    nodes = [i for i in range(n+1)]
    cost.sort(key = lambda x : x[2])
    
    for u, v, wt in cost:
        if find(u) != find(v):
            union(u, v)
            answer += wt

    return answer

n = 4
cost = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, cost))
```