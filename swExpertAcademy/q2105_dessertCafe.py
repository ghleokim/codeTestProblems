import sys
sys.stdin = open('input/input2105.txt', 'r')

"""
1
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
"""
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu

def checkOther(row,col,depth): # depth = 2부터
    res = []
    r = row + depth
    d = depth - 2
    for i in range(-d, d+1,2):
        c = col + i
        if c > 0 and c < N-1:
            res.append((r,c))
    return res

def makeSquare(start, end):
    k = 0
    searching = True

    # 꺾이는 점 찾기
    while searching:
        k += 1
        rowDelta = abs((start[0] + k) - end[0])
        colDelta = abs((start[1] + k) - end[1])
        if rowDelta == colDelta:
            searching = False

    res = []
    # path 탐색
    for i in range(0, k+1):
        res.append((start[0]+i, start[1]+i))
    for i in range(1,rowDelta+1):
        res.append((start[0]+k+i, start[1]+k-i))
    for i in range(1, k+1):
        res.append((end[0]-i,end[1]-i))
    for i in range(1,rowDelta):
        res.append((end[0]-k-i,end[1]-k+i))

    # 범위를 벗어나거나 빈 리스트 -> None
    for c in res:
        if any((c[0] < 0, c[0] >= N, c[1] < 0, c[1] >= N)):
            return None
    if not res:
        return None
    else:
        return res

def checkConflict(idx): # idx: [(r,c),(r,c),(r,c),... ]
    # 중복 검사
    if not idx:
        return False
    compare = set()
    for pos in idx:
        compare.add(board[pos[0]][pos[1]])
    if len(compare) == len(idx):
        return True
    else:
        return False
        

for T in range(int(input())):
    board = []
    res = []
    N = int(input())
    for i in range(N):
        tmp = list(map(int,input().split()))
        board.append(tmp)

    for row in range(0, N-1):
        for col in range(1, N):
            # print('row, col = ',end='')
            # print(row, col)
            for depth in range(2, N - row + 1):
                des = checkOther(row,col,depth)
                for end in des:
                    # print(makeSquare((row,col),end))
                    if checkConflict(makeSquare((row,col),end)):
                        res.append(makeSquare((row,col),end))

    if not res:
        result = -1
    else:
        result = len(max(res, key= lambda x: len(x)))
    print(result)



# Tester
# print(checkOther(3, 3, 3))
# print(checkOther(3, 3, 4))
# print(checkOther(3, 3, 5))
# print(checkOther(3, 3, 6))