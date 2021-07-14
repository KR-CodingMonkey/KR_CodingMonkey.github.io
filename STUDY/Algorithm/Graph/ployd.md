# 최단 경로 알고리즘(Ployd)

$$
\begin{aligned}
& D_(ij) = min(D_(ij), D_(ik) + D_(kj))
\end{aligned}
$$

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