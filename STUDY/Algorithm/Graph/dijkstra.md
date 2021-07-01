
# 최단 경로 알고리즘

- 다익스트라(Dijkstra Algorithm)
- 다익스트라 알고리즘은 greedy 알고리즘이며 단방향, 양방향(사이클) 모두 사용 가능
- 너비 우선 탐색(BFS) 방식과 유사

## 우선순위 큐

- 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산
- 더 긴 거리로 계산된 루트에 대해서는 계산을 스킵

```python
import heapq

def dijfstra(graph, start):
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
                distances[adjacent] = distances
                heapq.heapush(queue, [distance, adjacent])

    return distances
```