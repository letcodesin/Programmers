from tkinter import N


def solution(brown, yellow):
    answer = []
    ywidth = []
    yheight = []
    
    yhalflen = int(yellow / 2)
    if yellow <= 3:
        yhalflen = 2
    if yellow == 4:
        yhalflen = 3

    for i in range(1, yhalflen):
        if yellow % i == 0 and int(yellow/i) >= i:
            yheight.append(i)
            ywidth.append(int(yellow / i))

    i = len(yheight) - 1
    while i >= 0:
        if (yheight[i] + 2) * (ywidth[i] + 2) == (brown + yellow):
            answer.append(ywidth[i] + 2)
            answer.append(yheight[i] + 2)
            break
        i -= 1
    return answer

######################upgrade code##########################
def solution(brown, yellow):
    im = brown + yellow
    for i in range(1, im+1):
        if im % i != 0:
            continue
        m = im // i
        if (m-2)*(i-2) == yellow:
            return sorted([i, m], reverse = True)
