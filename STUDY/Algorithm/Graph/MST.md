

# 최소 신장 트리(Kruskal)

- 최소 신장 트리 (MST, Minimum Spanning Tree)
- 간선의 가중치 합이 최소인 Spanning Tree
- **Greedy Algorithm(탐욕법)**을 기초로 하고 있음


## 구현

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