def solution(citations):
    answer = 0
    candidaite = 0
    citations.sort()
    print(citations)
    for i in range(0, len(citations) + 1):
        j = 0
        bignum = 0
        while j < len(citations):
            if i <= citations[j]:
                bignum += 1
            j += 1
        #print(bignum)
        if i <= bignum:
            answer = i
    return answer


############upgrade code####################

def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        bignum = len(citations) - i #10 9 8 7 ....
        #print(bignum, citations[i])
        if citations[i] >= bignum:
            answer = bignum
            break
    return answer
    