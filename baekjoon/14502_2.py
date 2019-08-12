# https://www.acmicpc.net/problem/14502
"""
2차 배열 대신 1차 배열 사용
실행시간 1704ms -> 712ms
메모리 136768kb -> 126084kb
"""

def checkSides(coord):
    # returns list of 0 around (r,c) | Max 4
    side_list = []
    if coord >= M :                     # top
        if newboard[coord - M] == 0:
            side_list.append(coord - M)
    if coord < (N-1) * M:              # bottom
        if newboard[coord + M] == 0:
            side_list.append(coord + M)
    if coord % M != 0:                  # left
        if newboard[coord - 1] == 0:
            side_list.append(coord - 1)
    if coord % M != M-1:                # right
        if newboard[coord + 1] == 0:
            side_list.append(coord + 1)

    return side_list

def checkZero():
    # returns list of coordinates of zero in board
    zero_list = []
    for coord, val in enumerate(newboard):
        if val == 0:
            zero_list.append(coord)
    
    return zero_list


def spread():
    spread_list = []
    # define where to spread
    for coord, val in enumerate(newboard):
        if val == 2:
            spread_list.extend(checkSides(coord))

    if not spread_list:
        return 0
    else:
        for n in range(len(spread_list)):
            coord = spread_list.pop()
            # print(coord)
            newboard[coord] = 2
        spread()

def makeWall(walls):
    # walls: (c1, c2, c3)
    for coord in walls:
        newboard[coord] = 1

# inputs
N, M = map(int, input().split())

board = []
check_list = []

for n in range(N):
    row = list(map(int, input().split()))
    board.extend(row)
    # for en, num in enumerate(row):
    #     if num == 2:
    #         check_list.append(en)

newboard = board

# make list of all sets
zero_list = checkZero()
wall_list = []
for i in range(len(zero_list)):
    for j in range(i+1,len(zero_list)):
        for k in range(j+1, len(zero_list)):
            wall_list.append((i,j,k))      

# try for all chances in wall_list
result = 0
for walls in wall_list:
    # (w1, w2, w3) = walls
    wl = [zero_list[k] for k in walls]
    # print(wl)

    # shallow copy
    newboard = board[:]
    makeWall(wl)

    spread()
    zeros = len(checkZero())
    if zeros > result:
        result = zeros

print(result)