def solution(progresses, speeds):
    answer = []
    days = []
    stack = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            days.append(remain//speeds[i])
        else:
            days.append(remain//speeds[i] + 1)
    print(days)
    for i in range(len(days)):
        if len(stack) > 0 and max(stack) < days[i]:
            answer.append(len(stack))
            stack.clear()
        stack.append(days[i])
        #print(stack)
    answer.append(len(stack))
    return answer

#############################other solution####################

import math
def solution(progresses, speeds):
    answer = []
    queue = [] #남은날짜, 작업갯수
    for p, s in zip(progresses, speeds):
        if len(queue) == 0 or queue[-1][0] < math.ceil((100-p)/s):
            queue.append([math.ceil((100-p)/s), 1])
        else:
            queue[-1][1] += 1
    answer = [queue[i][1] for i in range(len(queue))]
    return answer

