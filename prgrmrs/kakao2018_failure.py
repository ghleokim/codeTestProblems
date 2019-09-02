# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    
    top = [0 for _ in range(N+2)]
    bottom = [0 for _ in range(N+2)]
    
    for s in stages:
        top[s] += 1
        for i in range(1,s+1):
            bottom[i] += 1  
            
    # print(top)
    # print(bottom)
    
    res = []
    for i in range(1,N+1):
        if bottom[i]:
            res.append((top[i]/bottom[i], i))
        else:
            res.append((0,i))
    
    for i in range(N-1):
        for j in range(i,N):
            if res[i][0] < res[j][0]:
                res[i], res[j] = res[j], res[i]
            elif res[i][0] == res[j][0] and res[i][1] >res[j][1]:
                res[i], res[j] = res[j], res[i]
        
    answer.extend([*zip(*res)][1])
    
    
    return answer