# https://www.acmicpc.net/problem/14502

from pprint import pprint
import copy

def checkSides(r, c, newboard):
    # returns list of 0 around (r,c) | Max 4
    side_list = []
    if r != 0:
        if newboard[r-1][c] == 0:
            side_list.append((r-1,c))
    if c != 0:
        if newboard[r][c-1] == 0:
            side_list.append((r,c-1))
    if r != N-1:
        if newboard[r+1][c] == 0:
            side_list.append((r+1,c))
    if c != M-1:
        if newboard[r][c+1] == 0:
            side_list.append((r,c+1))

    return side_list


def checkZero(newboard):
    # returns list of coordinates of zero in board
    zero_list = []
    for r, row in enumerate(newboard):
        for c, num in enumerate(row):
            if num == 0:
                zero_list.append((r,c))
    
    return zero_list


def spread(newboard):
    spread_list = []
    # define where to spread
    for r, row in enumerate(newboard):
        for c, num in enumerate(row):
            if newboard[r][c] == 2:
                spread_list.extend(checkSides(r,c, newboard))

    if not spread_list:
        return newboard
    else:
        for n in range(len(spread_list)):
            coord = spread_list.pop()
            # print(coord)
            newboard[coord[0]][coord[1]] = 2
        spread(newboard)


def makeWall(walls, newboard):
    # walls: ((r1,c1), (r2,c2), (r3,c3))
    for coord in walls:
        r, c = coord[0], coord[1]
        newboard[r][c] = 1

# inputs
N, M = map(int, input().split())

board = []
check_list = []

for n in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for en, num in enumerate(row):
        if num == 2:
            check_list.append((n,en))

# make list of all sets
zero_list = checkZero(board)
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

    # make a deep copy of the board
    new_board = copy.deepcopy(board)

    # make wall on three points
    makeWall(wl, new_board)

    # spread
    spread_board = spread(new_board)
    zeros = len(checkZero(new_board))
    if zeros > result:
        result = zeros
print(result)