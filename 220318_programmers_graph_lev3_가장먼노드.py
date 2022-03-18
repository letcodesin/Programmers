def solution(n, edge):
    answer = 0
    adjacent_list = [[]for _ in range(n)]
    for i in range(len(edge)):
        adjacent_list[edge[i][0]-1].append(edge[i][1]-1)
        adjacent_list[edge[i][1]-1].append(edge[i][0]-1)
    #print(adjacent_list)
    #bfs
    visited = [0 for _ in range(n)]
    queue = []
    dist = [0 for _ in range(n)]
    queue.append(0)
    visited[0] = 1
    while queue:
        current_node = queue.pop(0)
        for next_node in adjacent_list[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                dist[next_node] = dist[current_node] + 1
                queue.append(next_node)
    #print(dist)
    
    dist.sort(reverse=True)
    answer = dist.count(dist[0])
    
    return answer


##########################시간초과 풀이########################
def solution(n, edge):
    answer = 0
    adjacent_list = [[]for _ in range(n)]
    for i in range(len(edge)):
        adjacent_list[edge[i][0]-1].append(edge[i][1]-1)
        adjacent_list[edge[i][1]-1].append(edge[i][0]-1)
    #print(adjacent_list)
    #bfs
    visited_node = []
    queue = []
    dist = [0 for _ in range(n)]
    queue.append(0)
    visited_node.append(0)
    while queue:
        current_node = queue.pop(0)
        for next_node in adjacent_list[current_node]:
            if next_node not in visited_node:
                visited_node.append(next_node)
                dist[next_node] = dist[current_node] + 1
                queue.append(next_node)
    #print(dist)
    
    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1
    
    return answer