from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    result = []
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    #print(queue)
    while queue:
        maxque = max(queue, key=lambda x: x[1])
        if queue[0][1] < maxque[1]:
            queue.append(queue.popleft())
        else:
            result.append(queue.popleft())
    #print(result)
    for i in range(len(result)):
        if location == result[i][0]:
            answer = i + 1
            break
    return answer

##########################other solution##########################
def solution(priorities, location):
    answer = 0
    queue = [(index, prior) for index, prior in enumerate(priorities)]
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                break
    return answer

