#Kruskal 알고리즘 풀이

def solution(n, costs):
    answer = 0
    costs = sorted(costs, key = lambda x: x[2])
    print(costs)
    visited = set()
    visited.add(costs[0][0])
    while len(visited) != n:
        for cost in costs:
            if cost[0] in visited and cost[1] in visited:
                continue
            if cost[0] in visited or cost[1] in visited:
                visited.add(cost[0])
                visited.add(cost[1])
                answer += cost[2]
                break
    return answer

####################other solution###################

import heapq

def solution(n, costs):
    answer = 0
    adjacent = list(list() for _ in range(n))
    for cost in costs:
        adjacent[cost[0]].append([cost[1], cost[2]])
        adjacent[cost[1]].append([cost[0], cost[2]])
    visited = [0 for _ in range(n)]
    #print(adjacent)
    queue = []
    heapq.heappush(queue, [0,0])
    while 0 in visited:
        cost, start = heapq.heappop(queue)
        if visited[start] == 1:
            continue
        visited[start] = 1
        answer += cost
        for goto ,cost in adjacent[start]:
            if visited[goto] == 1:
                continue
            else:
                heapq.heappush(queue, [cost, goto])
    return answer
