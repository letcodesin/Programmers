def solution(m, n, puddles):
    for i in range(len(puddles)):
        puddles[i] = [puddles[i][1]-1, puddles[i][0]-1]#x, y좌표를 행과열 표현으로 바꿈
    dp = [[0] * m for _ in range(n)] #m = 4, n = 3 -> 3행 4열
    dp[0][0] = 1
    for j in range(1, m):
        if [0, j] in puddles:
            dp[0][j] = 0
        else:
            dp[0][j] = dp[0][j-1]
    for i in range(1, n):
        if [i, 0] in puddles:
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    print(dp)
    answer = dp[n-1][m-1] % 1000000007
    return answer

#참고: https://makefortune2.tistory.com/132

##########################upgrade solution############################

def solution(m, n, puddles):
    for i in range(len(puddles)):
        puddles[i] = [puddles[i][1], puddles[i][0]]#x, y좌표를 행과열 표현으로 바꿈
    dp = [[0] * (m+1) for _ in range(n+1)] #m = 4, n = 3 -> 3행 4열
    #계산의 편의를 위해 모든 값이 0인 행과 열 1개씩 추가
    dp[1][1] = 1 #[1,1]부터 길 시작
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue #초기값 dp[1][1] = 1로 시작
            if [i, j] in puddles: #웅덩이가 있는 경우
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    print(dp)
    answer = dp[n][m] % 1000000007
    return answer

#참고: https://dev-note-97.tistory.com/141