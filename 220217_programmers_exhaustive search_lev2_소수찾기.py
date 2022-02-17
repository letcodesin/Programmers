def solution(numbers):
    candidaite = []
    select_numbers = ''
    recursion_candidaite(select_numbers, numbers, candidaite)
    print(candidaite)
    answer = check_decimal(candidaite)
    
    return answer

def check_decimal(candidaite):
    answer = 0
    for i in range(0, len(candidaite)):
        if candidaite[i] != 0 and candidaite[i] != 1:
            mok = 0
            for j in range(2, candidaite[i]):
                if candidaite[i] % j == 0:
                    mok += 1
                if mok > 0:
                    break
            if mok == 0:
                answer += 1
    return answer

def recursion_candidaite(select_numbers,remain_numbers, candidaite):
    if select_numbers != '':
        num = int(select_numbers)
        if num not in candidaite: 
            candidaite.append(num)
        
    for j in range(0, len(remain_numbers)):
        recursion_candidaite(select_numbers + remain_numbers[j], 
                             remain_numbers[0:j] + remain_numbers[j+1:], candidaite)
    
         
     
##########################upgrade code#########################

prime_numbers = set()
def solution(numbers):
    select_numbers = ''
    recursion_candidaite(select_numbers, numbers)
    print(prime_numbers)
    return len(prime_numbers)

def check_decimal(candidaite):
    if candidaite != 0 and candidaite != 1:
        mok = 0
        for j in range(2, candidaite):
            if candidaite % j == 0:
                mok += 1
            if mok > 0:
                break
        if mok == 0:
            return True

def recursion_candidaite(select_numbers,remain_numbers):
    global prime_numbers
    if select_numbers != '':
        if check_decimal(int(select_numbers)): 
            prime_numbers.add(int(select_numbers))
        
    for j in range(0, len(remain_numbers)):
        recursion_candidaite(select_numbers + remain_numbers[j], 
                             remain_numbers[0:j] + remain_numbers[j+1:])
