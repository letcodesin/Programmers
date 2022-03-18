def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    low = 1 #돌사이의 거리 최솟값
    high = distance #돌사이의 거리 최댓값
    while low <= high:
        mid = (low + high) // 2
        pre_rock_position = 0 #돌사이의 거리 앞에 돌 위치
        delete_rock_count = 0 
        for i in range(len(rocks)):
            if rocks[i] - pre_rock_position < mid:
                delete_rock_count += 1 #mid보다 돌사이의 거리 작으면 제거
            else:
                pre_rock_position = rocks[i]
        if delete_rock_count > n: #제거된 돌이 n개보다 많으면 mid값 줄임
            high = mid - 1
        else: #제거된 돌이 n개보다 적거나 같으면
            answer = mid 
            low = mid + 1 #mid값 늘임
        
    return answer

#참고: https://m.post.naver.com/viewer/postView.nhn?volumeNo=27217004&memberNo=33264526
#참고: https://cocook.tistory.com/84