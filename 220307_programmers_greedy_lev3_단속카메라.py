def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    #print(routes)
    camera_position = -30001
    
    for route in routes:
        if camera_position < route[0]:
            answer += 1
            camera_position = route[1]
    
    return answer