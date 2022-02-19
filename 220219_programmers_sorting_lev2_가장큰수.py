def solution(numbers):
    answer = ''
    snum = []
    for n in numbers:
        snum.append(str(n))
    snum = sorted(snum, reverse = True)
    
    i = 0
    while i < len(snum) - 1:
        if i == -1:
            i = 0
        if snum[i] + snum[i+1] < snum[i+1] + snum[i]:
            snum[i] , snum[i+1] = snum[i+1] , snum[i] 
            i -= 1
            continue
        i += 1
    for i in range(0, len(snum)):
        answer += snum[i]
    answer = str(int(answer)) # in case 000000 => 0
    return answer

#####################upgrade code##########################

import functools

def xy_yx_compare(n1, n2):
    if n1+n2 > n2+n1:
        return 1
    elif n1+n2 < n2+n1:
        return -1
    else:
        return 0

def solution(numbers):
    answer = ''
    snum = []
    for n in numbers:
        snum.append(str(n))
    snum = sorted(snum, key = functools.cmp_to_key(xy_yx_compare), reverse = True)
    
    for i in range(0, len(snum)):
        answer += snum[i]
    answer = str(int(answer)) # in case 000000 => 0
    return answer




