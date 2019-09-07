# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    tmp = []
    answer = []
    data = {}
    ansA = '님이 들어왔습니다.'
    ansB = '님이 나갔습니다.'
    
    for row in record:
        r = row.split()
        # enter or change
        if len(r) == 3:
            message, key, value = r
            if message == 'Enter':
                data[key] = value
                tmp.append((1, key))
            else:
                data[key] = value
        # leave
        if len(r) == 2:
            message, key = r
            tmp.append((0, key))
    
    for t in tmp:
        if t[0]:
            answer.append((data[t[1]]+ansA))
        else:
            answer.append((data[t[1]]+ansB))
    
    return answer