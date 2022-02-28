def solution(N, number):
    answer = -1
    ST = []
    for i in range(1,9):
        nums = set()
        nums.add( int(str(N)*i) )
        for j in range(i-1):
            for x in ST[j]:
                for y in ST[i-j-2]:
                    nums.add(x + y)
                    nums.add(x - y)
                    nums.add(x * y)
                    if y != 0:
                        nums.add(x // y)
        if number in nums:
            answer = i
            break
            
        ST.append(nums)
    
    return answer