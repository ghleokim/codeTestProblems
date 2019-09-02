# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_XEokaAEcDFAX7&
# 이분탐색
# 시간이 있으면 해당 시간동안 통과한 사람의 수를 알 수 있다.

def solution(n, times):    
    left = 1
    right = n * max(times) + 1
    
    while left <= right:
        mid = (left+right) // 2
        
        res = 0
        for i in range(len(times)):
            res += mid // times[i]
            
        if res < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

for T in range(int(input())):
    N, M = map(int,input().split())
    t = []
    for i in range(N):
        t.append(int(input()))

    print('#',end='')
    print(T+1,solution(M,t))
