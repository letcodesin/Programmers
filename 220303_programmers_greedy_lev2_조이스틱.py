#주의 케이스: BBBAAABB move=6 , BABBAAAB move = 6
def solution(name):
    answer = 0
    move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        if name[i] == 'A':
            left = i-1
            if i == 0:
                left = 0
            a_idx = i + 1
            while a_idx < len(name) and name[a_idx] == 'A':
                a_idx += 1
            right = len(name) - a_idx
            move = min(move, left + min(left, right) + right)
    answer += move
    return answer

#참고: https://bellog.tistory.com/152
#참고: https://velog.io/@heering_/%EA%B7%B8%EB%A6%AC%EB%94%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV2.-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1