def solution(n, times):
    times.sort()
    low = 1
    high = times[0] * n
    answer = high
    while low <= high:
        mid = (low + high) // 2
        pcount = 0
        for time in times:
            pcount += mid // time
        if pcount >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer