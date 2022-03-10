import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)
    newk = heap[0]
    while newk < K and len(heap) > 1:
        newk = heapq.heappop(heap)
        hpop = heapq.heappop(heap)
        newk = newk + (hpop * 2)
        heapq.heappush(heap, newk)
        newk = heap[0]
        answer += 1
    if heap[0] < K:
        answer = -1
    return answer

####################other solution########################

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    newk = scoville[0]
    while newk < K:
        newk = heapq.heappop(scoville)
        if len(scoville) == 0:
            return -1
        hpop = heapq.heappop(scoville)
        newk = newk + (hpop * 2)
        heapq.heappush(scoville, newk)
        newk = scoville[0]
        answer += 1
    return answer
