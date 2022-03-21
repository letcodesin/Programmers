def solution(money):
    answer = 0
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):#첫번째 집을 포함하고 마지막 집을 포함하지 않은 경우
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    #print(dp)

    dp1 = [0] * len(money)
    dp1[0] = 0
    dp1[1] = money[1]
    for i in range(2, len(money)):#첫번째 집을 포함하지 않은 경우
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
    #print(dp1)
    answer = max(dp[-2], dp1[-1])
    return answer

#참고: https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://mjmjmj98.tistory.com/109