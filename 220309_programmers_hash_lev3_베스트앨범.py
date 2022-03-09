from collections import defaultdict
def solution(genres, plays):
    answer = []
    hcount = defaultdict(int)
    hash_map = dict()
    for i in range(len(genres)):
        hcount[genres[i]] += plays[i]
        numidx = [plays[i], i]
        if genres[i] not in hash_map:
            hash_map[genres[i]] = [numidx]
        else:
            hash_map[genres[i]].append(numidx)
    #print(hash_map)
    #print(hcount)
    hcount = sorted(hcount.items(),key = lambda x: x[1], reverse = True)
    #print(hcount)
    for key in hash_map:
        hash_map[key] = sorted(hash_map[key], key = lambda x : (-x[0], x[1]))
        #hash_map[key].sort(reverse = True)
    #print(hash_map)
    for i in range(len(hcount)):
        added = 0
        for hm in hash_map[hcount[i][0]]:
            added += 1
            answer.append(hm[1])
            if added == 2:
                break
    return answer

###############################################################
from collections import defaultdict
def solution(genres, plays):
    answer = []
    hcount = defaultdict(int)
    hash_map = dict()
    for i in range(len(genres)):
        hcount[genres[i]] += plays[i]
        numidx = [plays[i], i]
        if genres[i] not in hash_map:
            hash_map[genres[i]] = [numidx]
        else:
            hash_map[genres[i]].append(numidx)
    hcount = sorted(hcount.items(),key = lambda x: x[1], reverse = True)
    for key in hash_map:
        hash_map[key] = sorted(hash_map[key], key = lambda x : (-x[0], x[1]))
    for i in range(len(hcount)):
        answer.extend(x[1] for x in hash_map[hcount[i][0]][:2])
    return answer