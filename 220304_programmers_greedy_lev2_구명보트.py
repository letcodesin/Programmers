
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        else:
            people.pop()
            answer += 1
    return answer + len(people)


#####################효율적 풀이#######################
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


######################비효율적 풀이####################

def solution(people, limit):
    answer = 0
    while len(people) > 1:
        maxperson = max(people)
        minperson = min(people)
        if maxperson + minperson > limit:
            answer += 1
            midx = people.index(maxperson)
            people = people[:midx] + people[midx+1:]
        else:
            maxidx = people.index(maxperson)
            people = people[:maxidx] + people[maxidx+1:]
            minidx = people.index(minperson)
            people = people[:minidx] + people[minidx+1:]
            answer += 1
    return answer + len(people)

#######################비효율적 풀이2###################
def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop()
            answer += 1
        else:
            people.pop()
            answer += 1
    return answer + len(people)