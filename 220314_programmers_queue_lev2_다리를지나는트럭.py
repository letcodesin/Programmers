def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return answer

####################other solution#######################
from collections import deque
def solution(bridge_length, weight, truck_weights):
    on_bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    answer = 0
    while truck_weights:
        total_weight -= on_bridge.popleft()
        if total_weight + truck_weights[0] <= weight:
            cur_truck = truck_weights.pop(0)
            on_bridge.append(cur_truck)
            total_weight += cur_truck
        else:
            on_bridge.append(0)
        answer += 1
    answer += bridge_length #마지막 트럭이 지나가는 시간
    return answer

###################wrong solution 잘못된 풀이, 접근 방식###################
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    count = 0
    i = 0
    for i in range(len(truck_weights)):
        if  bridge_length > count and weight > total_weight:
            count += 1
            total_weight += truck_weights[i]
            answer += 1
        else:
            total_weight = 0
            count = 0
            answer += bridge_length
    answer += bridge_length
    return answer