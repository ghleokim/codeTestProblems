def solution(dartResult):
    answer = 0
    N = len(dartResult)
    dartidx = 0
    ci = -1
    
    score = [0 for _ in range(N)]
    exp = [0 for _ in range(N)]
    multiplier = [1 for _ in range(N)]
    
    while dartidx != len(dartResult):
        token = dartResult[dartidx]
        if token.isdigit():
            if dartResult[dartidx-1].isdigit():
                score[ci] = 10
            else:
                ci += 1
                score[ci] = int(token)
        elif token.isalpha():
            if token == 'S':
                exp[ci] = 1
            elif token == 'D':
                exp[ci] = 2
            else:
                exp[ci] = 3
        elif token == '*':
            if dartidx:
                multiplier[ci] *= 2
                multiplier[ci-1] *= 2
            else:
                multiplier[ci] *= 2
        else:
            multiplier[ci] *= -1
            
        dartidx += 1

    for i in range(N):
        if exp[i] == 0: break
        answer += (score[i] ** exp[i]) * multiplier[i]
    
    return answer