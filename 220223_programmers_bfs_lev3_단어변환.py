import heapq 

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  

    while queue: 
        current_distance, current_destination = heapq.heappop(queue) 

        if distances[current_destination] < current_distance: 
            continue

        for new_destination in graph[current_destination]:
            distance = current_distance + 1 
            if distance < distances[new_destination]:  
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])    
    return distances


def solution(begin, target, words):
    answer = 0
    graph = dict()
    words.append(begin)
    for t in range(len(words)):
        candidaite = []
        for i in range(len(words)):
            diff = 0
            for j in range(len(begin)):
                if words[t][j] != words[i][j]:
                    diff += 1
            if diff == 1:
                candidaite.append(words[i])
        graph[words[t]] = candidaite
    print(graph)
    distance = dijkstra(graph, begin)
    
    for node, dist in distance.items():
        if node == target:
            answer = dist
    
    return answer


########################other solution######################

def get_adjacent(node, words):
    neighbors = []
    for word in words:
        diff = 0
        for i in range(len(node)):
            if word[i] != node[i]:
                diff += 1
        if diff == 1:
            neighbors.append(word)
    return neighbors
def solution(begin, target, words):
    answer = 0
    visited = {begin: 0}
    for word in words:
        visited[word] = 0
    
    dist = {begin: 0}
    for word in words:
        dist[word] = 0
    
    queue = [begin]
    while queue:
        node = queue.pop(0)
        for neighbor in get_adjacent(node, words):
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    print(visited)
    print(dist)
    answer = dist.get(target, 0)
    return answer    