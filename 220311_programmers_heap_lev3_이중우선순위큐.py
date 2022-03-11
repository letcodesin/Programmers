def insertion(heap, num):
    i = 0
    while i < len(heap) and heap[i] < num:
        i += 1
    heap.insert(i, num)
    #print(heap)
def solution(operations):
    answer = []
    heap = []
    for oper in operations:
        if oper == "D 1": 
            if len(heap) > 0:
                heap.pop()
        elif oper == "D -1":
            if len(heap) > 0:
                heap.pop(0)
        else:
            num = int(oper[2:])
            insertion(heap, num)
    #print(heap)
    if len(heap) > 1:
        answer.append(heap[-1])
        answer.append(heap[0])
    else:
        answer = [0,0]
    return answer

#####################other solution####################
import heapq
def solution(operations):
    answer = []
    heap = []
    for operat in operations:
        front, back = operat.split(' ')
        if front == "I":
            heapq.heappush(heap, int(back))
        elif len(heap) > 0:
            if back == "-1":
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)
    if len(heap) > 0:
        answer.append(max(heap))
        answer.append(heap[0])
    else:
        answer = [0,0]
    return answer
    