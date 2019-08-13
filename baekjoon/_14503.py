# https://www.acmicpc.net/problem/14503
"""

"""

from pprint import pprint

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# check wall: check if direction is wall or not
def checkWall(p, d):
    r = p[0] + direction[d][0]
    c = p[1] + direction[d][1]

    if board[r][c] == 1:
        return False
    else:
        return True

# check dirty: check if direction is dirty
def checkDirty(p, d):
    r = p[0] + direction[d][0]
    c = p[1] + direction[d][1]

    if board[r][c] == 2:
        return False
    else:
        return True

def move(p, d):
    r = p[0] + direction[d][0]
    c = p[1] + direction[d][1]

    return (r, c)

def back(p, d):
    d = (d + 2) % 4
    r = p[0] + direction[d][0]
    c = p[1] + direction[d][1]

    return (r, c)

N, M = map(int, input().split())
R, C, D = map(int, input().split())
board = []

for row in range(N):
    board.append(list(map(int, input().split())))

cnt = 1
board[R][C] = 2
# left: (D+3) % 4
rotate = 0
wall = 0
pos = (R, C)

while True:
    if rotate >= 4 and back(pos,D) != 1:
        pos = back(pos, D)
    elif wall >= 4:
        break

    # clean current position
    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = 2
        cnt += 1
        print('count=',end='')
        print(cnt)
        pprint(board)

    # see left
    left = (D + 3) % 4
    print(pos, left)

    if checkWall(pos, left):
        print('rotate=', end='')
        print(rotate, end=' ')
        print('wall=', end='')
        print(wall)
        if checkDirty(pos, left):
            pos = move(pos, left)
            D = left
            wall, rotate = 0, 0
            print(cnt, pos, D)
            # pprint(board)
            continue
        else:
            D = left
            print(D)
            rotate += 1
            continue
            
    else:
        print(wall)
        D = left
        rotate += 1
        wall += 1
        continue
    
print(cnt)