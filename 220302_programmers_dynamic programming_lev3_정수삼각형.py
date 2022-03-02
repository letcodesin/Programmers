def solution(triangle):
    answer = 0
    tsum = []
    tsum.append(triangle[0])
    for i in range(1, len(triangle)):
        line = []
        for j in range(0, len(triangle[i])):
            if j == 0:
                line.append(tsum[i-1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                line.append(tsum[i-1][j-1] + triangle[i][j])
            else:
                num = tsum[i-1][j-1] + triangle[i][j]
                if num < tsum[i-1][j] + triangle[i][j]:
                    num = tsum[i-1][j] + triangle[i][j]
                line.append(num)
        tsum.append(line)
    answer = max(tsum[len(tsum)-1])
    return answer

#########################upgrade solution####################

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])
    answer = max(triangle[-1])
    return answer