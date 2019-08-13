"""
11 10
1 1 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""

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

originalD = D
rotate = 1
en = 0
cnt = 0
pos = (R, C)

while True:
    #en += 1

    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = 2
        cnt += 1

    left = (D + 3) % 4
    # check wall on the left:
    # if empty, check dirty
        # if dirty, move point
        # if not dirty, rotate
        # if not dirty and rotated more than 4,
            # check if back is wall
                # if back is wall, break
                # if back is not wall, move back / rotate = 0
    # if wall, rotate

    if checkWall(pos,left):
        if rotate >= 4:
            bck = back(pos, originalD)
            if board[bck[0]][bck[1]] == 1:
                break
            else:
                pos = bck
                rotate = 0
        elif checkDirty(pos,left):
            pos = move(pos,left)
            D = left
            originalD = D
            rotate = 0
        
        else:
            D = left
            rotate += 1
    else:
        D = left
        rotate += 1
        if rotate >= 4:
            bck = back(pos, originalD)
            if board[bck[0]][bck[1]] == 1:
                break
            else:
                pos = bck
                rotate = 0

print(cnt)