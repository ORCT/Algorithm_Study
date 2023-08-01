import heapq
import sys
ssr = sys.stdin.readline

INF = 987654321  # any big number that over the input limit
    
def dijkstra(vertex, edges, start, end): # 1. set the start node.
    
    def get_nearest_node():
        min_distance = INF
        nearest_node = 0
        for i in range(1, vertex+1):
            if distance[i] < min_distance and visited[i] == False:
                nearest_node = i
        return nearest_node
    
    distance = [INF for _ in range(vertex+1)] # 2. initialize the distance array.
    visited = [False for _ in range(vertex+1)]
    distance[start] = 0
    for _ in range(vertex):
        cur_node = get_nearest_node() # 3. select the nearest node.
        visited[cur_node] = True
        for next_node, next_distance in edges[cur_node]:
            if distance[cur_node]+next_distance < distance[next_node]:
                distance[next_node] = distance[cur_node]+next_distance # 4. update min distance
    return distance[end]
    
def improved_dijkstra(vertex, edges, start, end):
    h = []
    heapq.heappush(h, (0, start))
    distance = [INF for _ in range(vertex+1)] # 2. initialize the distance array.
    distance[start] = 0
    while h:
        cur_distance, cur_node = heapq.heappop(h) # 3. select the nearest node.
        if cur_distance < distance[cur_node]:
            continue
        for next_node, next_distance in edges[cur_node]:
            if distance[cur_node]+next_distance < distance[next_node]:
                distance[next_node] = distance[cur_node]+next_distance # 4. update min distance
                heapq.heappush(h, (distance[next_node], next_node))
    return distance[end]

v, e = map(int, ssr().split())
edges = [[] for _ in range(v+1)]
for _ in range(e):
    departure, arrival, distance = map(int, ssr().split())
    edges[departure].append((arrival, distance))
start, end = map(int, ssr().split())
print(dijkstra(v, edges, start, end))
print(improved_dijkstra(v, edges, start, end))
    
'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

3 6
1 2 5
1 3 3
2 1 5
2 3 -4
3 1 3
3 2 -4
1 3
'''