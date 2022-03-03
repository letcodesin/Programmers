def solution(n, lost, reserve):
    answer = 0
    clouth = [1 for _ in range(n)]
    for i in lost:
        clouth[i-1] -= 1
    for i in reserve:
        clouth[i-1] += 1
    for i in range(n):
        if clouth[i] <= 0:
            if i-1 >= 0 and clouth[i-1] >=2:
                clouth[i-1] -= 1
                clouth[i] += 1
            elif i+1 < n and clouth[i+1] >=2:
                clouth[i+1] -= 1
                clouth[i] += 1
    for i in range(n):
        if clouth[i] >= 1:
            answer += 1
    return answer

#################upgrade solution################
def solution(n, lost, reserve):
    answer = 0
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)
    for r in sorted(new_reserve):
        if r-1 in new_lost:
            new_lost = new_lost - {r-1}
        elif r+1 in new_lost:
            new_lost = new_lost - {r+1}
    answer = n - len(new_lost)
    return answer