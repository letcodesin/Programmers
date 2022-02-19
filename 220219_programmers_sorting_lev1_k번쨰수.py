def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        sarray = array[commands[i][0] - 1:commands[i][1]]
        sarray.sort()
        answer.append(sarray[commands[i][2] - 1])
    return answer