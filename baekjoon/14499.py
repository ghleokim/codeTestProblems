#크기가 n*m인 지도
#   2
# 4 1 3
#   5
#   6

# direction
#   3
# 2 0 1
#   4

# dice [top,down], [east,west], [north,south]

#             0 1 2 3 4 5
# diceList = [1,6,3,4,2,5]

def checkEdge(direction, pos):
    if direction == 1 and pos[0] == pos[3]: # east
        return False
    elif direction == 2 and pos[0] == 0:    # west
        return False
    elif direction == 3 and pos[1] == 0:     # north
        return False
    elif direction == 4 and pos[1] == pos[2]: # south
        return False
    else:
        return True

def movePos(direction, pos):
    if direction == 1:    # east
        pos[0] += 1
    elif direction == 2:  # west
        pos[0] -= 1
    elif direction == 3:  # north
        pos[1] -= 1
    else:  # south
        pos[1] += 1
    return None

def moveDice(direction, *dice):
    if direction == 1:          # east
        td = (dice[3], dice[2])
        ew = (dice[0], dice[1])
        ns = (dice[4], dice[5])

    elif direction == 2:        # west
        td = (dice[2], dice[3])
        ew = (dice[1], dice[0])
        ns = (dice[4], dice[5])

    elif direction == 3:        # north
        td = (dice[5], dice[4])
        ew = (dice[2], dice[3])
        ns = (dice[0], dice[1])

    else:                       # south
        td = (dice[4], dice[5])
        ew = (dice[2], dice[3])
        ns = (dice[1], dice[0])

    return [*td,*ew,*ns]

def changeBottom(pos, dice):
    if mapNM[pos[1]][pos[0]]:
        dice[1] = mapNM[pos[1]][pos[0]]
        mapNM[pos[1]][pos[0]] = 0
    else:
        mapNM[pos[1]][pos[0]] = dice[1]

dice = [0]*6

n, m, x, y, k = map(int, input().split())

mapNM = []
for row in range(n):
    mapNM.append(list(map(int, input().split())))

move = list(map(int, input().split())) 

pos = [y, x, n-1, m-1]

for mov in move:
    # print(f'move: {mov}')
    # print(f'pos: {pos}')
    # print(f'dice: {dice}')
    if checkEdge(mov, pos):
        dice = moveDice(mov, *dice)
        movePos(mov, pos)
        changeBottom(pos, dice)
        print(dice[0])

# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2