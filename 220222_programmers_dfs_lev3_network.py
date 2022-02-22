def solution(n, computers):
    answer = 0
    visited = []
    for i in range(n):
        visited.append(0)
    def dfs(visited, computers, start):
        stack = []
        stack.append(start)
        while stack:
            node = stack.pop()
            if visited[node] == 0:
                visited[node] = 1
                for i in range(n):
                    if i != node and computers[i][node] == 1 and visited[i] == 0:
                        stack.append(i)
    
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(visited, computers, i)
            answer += 1
        i += 1
    
    return answer

#####################other solution###############
def dfs(i, n, visited, computers):
    for j in range(n):
        if (j != i) and (visited[j] == 0) and (computers[i][j] == 1):
            visited[j] = 1
            dfs(j, n, visited, computers)
        
def solution(n, computers):
    answer = 0
    visited = []
    for i in range(n):
        visited.append(0)
    for i in range(n):
        if visited[i] == 1:
            continue
        answer += 1
        dfs(i, n, visited, computers)
    return answer