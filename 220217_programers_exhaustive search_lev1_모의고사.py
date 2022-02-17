def solution(answers):
    answer = []
    correct = [[1,0],[2,0],[3,0]]
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(0, len(answers)):
        if ans1[int(i % len(ans1))] == answers[i]:
            correct[0][1] += 1
        if ans2[int(i % len(ans2))] == answers[i]:
            correct[1][1] += 1
        if ans3[int(i % len(ans3))] == answers[i]:
            correct[2][1] += 1
    correct = sorted(correct, key = lambda x: -x[1])
    print(correct)
    i = 0

    while i < len(correct) and correct[i][1] == correct[0][1]:
        answer.append(correct[i][0])
        i += 1
    return answer