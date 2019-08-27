# https://www.acmicpc.net/problem/15685
# 드래곤커브
# 117928 kb | 132 ms
dx = (1,  0, -1,  0) # col
dy = (0, -1,  0, 1) # row

S = 101

board = [[0 for _ in range(S)] for __ in range(S)]


def curve(d, g):
    count = 0
    res = [d]
    while count < 2 ** g:
        for r in res[::-1]:
            res.append((r+1) % 4)
        count = len(res)
    
    return res

def checkBoundary(x, y):
    if x < 0 or y < 0 or x == S or y == S:
        return False
    return True

def color(x, y, d, g):
    if not board[y][x]:
        board[y][x] = 1

    path = curve(d,g)

    for i in range(2**g):
        idx = path[i]
        x += dx[idx]
        y += dy[idx]
        if checkBoundary(x, y):
            if not board[y][x]: board[y][x] = 1

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    color(x, y, d, g)

result = 0

for i in range(S-1):
    for j in range(S-1):
        if board[i][j]:
            if board[i+1][j]:
                if board[i][j+1]:
                    if board[i+1][j+1]:
                        result += 1

print(result)


# 방법2: min, max 계산 후 마지막 검사 boundary 설정
# 118040 kb | 132 ms

dx = (1,  0, -1,  0) # col
dy = (0, -1,  0, 1) # row

S = 101
minX, minY, maxX, maxY = S, S, 0, 0

board = [[0 for _ in range(S)] for __ in range(S)]


def curve(d, g):
    count = 0
    res = [d]
    while count < 2 ** g:
        for r in res[::-1]:
            res.append((r+1) % 4)
        count = len(res)
    
    return res


def checkBoundary(x, y):
    if x < 0 or y < 0 or x == S or y == S:
        return False
    return True


def color(x, y, d, g):
    if not board[y][x]:
        minmax(x,y)
        board[y][x] = 1

    path = curve(d,g)

    for i in range(2**g):
        idx = path[i]
        x += dx[idx]
        y += dy[idx]
        minmax(x,y)
        if checkBoundary(x, y):
            if not board[y][x]: board[y][x] = 1


def minmax(x, y):
    global minX, minY, maxX, maxY
    if x < minX:
        minX = x
    if x > maxX:
        maxX = x
    if y < minY:
        minY = y
    if y > maxY:
        maxY = y
    
                
                
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    color(x, y, d, g)

result = 0

for i in range(minY, maxY):
    for j in range(minX, maxX):
        if board[i][j]:
            if board[i+1][j]:
                if board[i][j+1]:
                    if board[i+1][j+1]:
                        result += 1

print(result)