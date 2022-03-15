def solution(prices):
    answer = []
    for i in range(len(prices)):
        j = i + 1
        period = 0
        while j < len(prices):
            period += 1
            if prices[i] > prices[j]:
                break
            j += 1
        answer.append(period)
    return answer

#####################wrong solution######################
#반례: [1, 3, 5, 7, 9, 4, 5, 2, 1, 0] / [9, 6, 3, 2, 1, 2, 1, 1, 1, 0] 
def solution(prices):
    answer = []
    for i in range(len(prices)):
        j = i + 1
        period = 0
        while j < len(prices) and prices[i] <= prices[j]:
            j += 1
            period += 1
        if period == 0 and i < len(prices) - 1 and prices[i] > prices[i+1]:
            period = 1
        answer.append(period)
    return answer