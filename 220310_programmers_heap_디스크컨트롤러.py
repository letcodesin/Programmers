def solution(jobs):
    answer = 0
    spend_time = []
    current_time = 0
    jobs.sort(key = lambda x: (x[0], x[1]))
    spend_time.append(current_time)
    for i in range(0, len(jobs)):
        heap = []
        j = i
        while j < len(jobs) and jobs[j][0] <= current_time :
            heap.append(jobs[j])
            j += 1
        if len(heap) == 0:
            spend_time.append(jobs[i][1])
            current_time = jobs[i][0] + jobs[i][1]
        else:
            heap.sort(key = lambda x: x[1])
            #print(heap)
            jobs[i:j] = heap
            #print(jobs)
            spend_time.append(current_time + jobs[i][1] - jobs[i][0])
            #print(spend_time)
            current_time += jobs[i][1]
    tsum = 0
    for time in spend_time:
        tsum += time
    answer = tsum // len(jobs) 
    return answer

###########################other solution#######################
import heapq
from collections import deque
def solution(jobs):
    answer = 0
    total_spend_time = 0
    current_time = 0
    tasks = [(x[1],x[0]) for x in jobs] #실행시간, 시작시간
    #print(tasks)
    tasks.sort(key = lambda x: (x[1], x[0])) #시작시간 정렬 후 실행시간 정렬
    tasks = deque(tasks)
    #print(tasks)
    #tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    heap = []
    heapq.heappush(heap, tasks.popleft())
    while len(heap) > 0:
        itask = heapq.heappop(heap)
        current_time = max(current_time + itask[0], itask[1] + itask[0])
        total_spend_time += current_time - itask[1]
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(heap, tasks.popleft())
        if len(tasks) > 0 and len(heap) == 0:
            heapq.heappush(heap, tasks.popleft())
    answer = total_spend_time // len(jobs)
    return answer