#https://programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    day=list(map(lambda x: math.ceil((100 - x[0])/x[1]), zip(progresses,speeds)))
    answer = [1]

    q1 = day.pop(0)
    q2 = day.pop(0)

    while day:
        if q1 >= q2:
            answer[-1] += 1
            q2 = day.pop(0)
        else:
            answer.append(1)
            q1, q2 = q2, day.pop(0)
    
    if q1 >= q2:
            answer[-1] += 1
        else:
            answer.append(1)


    return answer

print(solution([93,30,55],[1,30,5]))