from collections import defaultdict

def dfs(graph, ticketnum, at, route):
    if ticketnum + 1 == len(route):
        return route
    for index, goto in enumerate(graph[at]):
        graph[at].pop(index)
        result = dfs(graph, ticketnum, goto, route + [goto])
        graph[at].insert(index, goto)
        if result:
            return result

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for key in graph:
        graph[key].sort()
    print(graph)
    route = ['ICN']
    for index, goto in enumerate(graph['ICN']):
        print(index, goto)
    answer = dfs(graph, len(tickets), 'ICN' ,route)                    
    return answer

#######################upgrade solution#####################

from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for key in graph:
        graph[key].sort()
    #print(graph)
    route = []
    stack = ['ICN']
    while stack:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            route.append(stack.pop())
        else:
            stack.append(graph[top][0])
            graph[top] = graph[top][1:]
    route.reverse()
    answer = route
    return answer

#########################wrong solving####################
def solution(tickets):
    answer = []
    graph = dict()
    for i in range(len(tickets)):
        if tickets[i][0] in graph:
            graph[tickets[i][0]].append(tickets[i][1])
            continue
        graph[tickets[i][0]] = [tickets[i][1]]
    print(graph)
    for key in graph:
        graph[key].sort()
    print(graph)
    queue = []
    queue.append('ICN')
    while queue:
        at = queue.pop(0)
        answer.append(at)
        if at in graph:
            for goto in graph[at]:
                queue.append(goto)
                graph[at].remove(goto)
                    
    return answer

