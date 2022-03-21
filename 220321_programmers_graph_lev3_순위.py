from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    for i in range(len(results)):
        win[results[i][0]-1].add(results[i][1]-1)
        lose[results[i][1]-1].add(results[i][0]-1)
    #print(win)
    #print(lose)
    for i in range(n):
        for loser in lose[i]:
            win[loser].update(win[i])
        for winner in win[i]:
            lose[winner].update(lose[i])
    #print(win)
    #print(lose)
    for i in range(n):
        if len(win[i]) + len(lose[i]) == n-1:
            #print(i)
            answer += 1
    return answer