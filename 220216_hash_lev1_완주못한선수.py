def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    i = 0
    j = 0
    while j < len(completion):
        if participant[i] != completion[j]:
            answer += participant[i]
            j = j - 1
        i += 1
        j += 1
    while i < len(participant):
        answer += participant[i]
        i += 1
    return answer