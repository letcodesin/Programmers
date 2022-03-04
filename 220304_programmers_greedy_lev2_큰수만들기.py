def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while k > 0 and len(stack) > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    answer = ''.join(stack[:len(number)-k])
    return answer

##########################시간초과 풀이1###########################

def max_idx(nums, start, finish):
    i = start
    midx = start
    while i < finish:
        if nums[midx] < nums[i]:
            midx = i
        i += 1
    return midx
def solution(number, k):
    answer = ''
    nums = list(map(int, number))
    #print(nums)
    remain = len(number) - k
    start = 0
    while remain > 0:
        midx = max_idx(nums,start, len(number) - remain)
        start = midx + 1
        if nums[midx] < nums[len(number) - remain]:
            answer += ''.join(map(str, nums[len(number) - remain:]))
            break
        answer += str(nums[midx])
        remain -= 1
    return answer

##########################시간초과 풀이2###########################

def max_idx(nums, start, finish):
    midx = nums[start:finish].index(max(nums[start:finish]))
    return start + midx
def solution(number, k):
    answer = ''
    nums = list(map(int, number))
    #print(nums)
    remain = len(number) - k
    start = 0
    while remain > 0:
        midx = max_idx(nums,start, len(number) - remain)
        start = midx + 1
        if nums[midx] < nums[len(number) - remain]:
            answer += ''.join(map(str, nums[len(number) - remain:]))
            break
        answer += str(nums[midx])
        remain -= 1
    return answer
