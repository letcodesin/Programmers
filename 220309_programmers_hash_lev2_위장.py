from collections import defaultdict

def solution(clothes):
    answer = 1
    hash_map = defaultdict(int)
    for clothe in clothes:
        hash_map[clothe[1]] += 1
    for key in hash_map:
        hash_map[key] += 1
    
    #print(hash_map)
    for key in hash_map:
        answer *= hash_map[key]
    answer -= 1
    return answer