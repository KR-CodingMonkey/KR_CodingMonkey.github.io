# 최단 경로 알고리즘(Ployd)

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
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

n = 4
data = [[1,3,-2],[2,1,4],[2,3,3],[3,4,2],[4,2,-1]]
print(Floyd_warshall(n, data))
```