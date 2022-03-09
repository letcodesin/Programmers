def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        next = phone_book[i+1]
        if phone_book[i] == next[:len(phone_book[i])]:
            #print(phone_book[i], next[:len(phone_book[i])])
            answer = False
            break
    #print(phone_book)
    return answer

#####################hash solution#########################
def solution(phone_book):
    answer = True
    hash_map = dict()
    for phone in phone_book:
        hash_map[phone] = 1
    #print(hash_map)
    for phone in phone_book:
        nums = ""
        for num in phone:
            nums += num
            #print(nums)
            if nums in hash_map and nums != phone:
                return False
    return answer