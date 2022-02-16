answer = 0
def solution(numbers, target):
    recursion_plus(0, numbers, target, 0)
    return answer

def recursion_plus(index, numbers, target, sum):
    global answer
    if index == len(numbers):
        if sum == target:
            answer += 1
        return 0
    recursion_plus(index+1, numbers, target, sum + numbers[index])
    recursion_plus(index+1, numbers, target, sum - numbers[index])
