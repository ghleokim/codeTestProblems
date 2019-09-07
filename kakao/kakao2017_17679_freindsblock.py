A = [
    [0,0,0],
    [1,1,1],
    [1,1,1],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [1,1,1],
    [0,0,0]
    ]
B = [
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4],
    [5,5,5],
    [6,6,6],
    [7,7,7],
    [8,8,8]
    ]

from pprint import pprint

def falldown():
    for k in range(len(A[0])):
        for i in range(len(A)-1,0,-1):
            if A[i][k]:
                print((i, k), end='')
                for j in range(i-1,-1,-1):
                    print((j, k), end='')
                    if not A[j][k]:
                        A[i][k], A[j][k] = A[j][k], A[i][k]
                        B[i][k], B[j][k] = B[j][k], B[i][k]
                        pprint(A)
                        pprint(B)
                        break
                else:
                    for j in range(0, i+1):
                        A[j][k] = 0
                        B[j][k] = 0
                    break
        
    pprint(A)
    pprint(B)

falldown()

def solution(m, n, board):
    answer = 0
    
    board = [[*board[i]] for i in range(m)]
    
    dx = (1,1,0)
    dy = (0,1,1)
    
    finished = False
    
    while not finished:
        finished = True
        cnt = 0
        matched = [[0 for _ in range(n)] for __ in range(m)]

        # check match
        for i in range(m-1):
            for j in range(n-1):
                skip = False
                cur = board[i][j]
                if not cur: continue
                for k in range(3):
                    ni,nj = i+dx[k], j+dy[k]
                    if board[ni][nj] != cur:
                        skip = True
                        continue
                if skip: continue
                else:
                    finished = False
                matched[i][j] = 1
                for k in range(3):
                    ni,nj=i+dx[k],j+dy[k]
                    matched[ni][nj] = 1

        # count matched
        for i in range(m):
            for j in range(n):
                if matched[i][j]: cnt += 1
                    
        # falldown
        for k in range(n):
            for i in range(m-1,0,-1):
                if matched[i][k]:
                    for j in range(i-1,-1,-1):
                        if not matched[j][k]:
                            matched[i][k], matched[j][k] = matched[j][k], matched[i][k]
                            board[i][k], board[j][k] = board[j][k], board[i][k]
                            break
                    else:
                        for j in range(0, i+1):
                            board[j][k] = 0
                            board[j][k] = 0
                        break
                        
        answer += cnt
        
    return answer