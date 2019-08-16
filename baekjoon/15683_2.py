from pprint import pprint
from copy import deepcopy

direction = [(0,1), (-1,0), (0,-1), (1,0)]

# countlist: 1,2,3,4,5 각 cctv의 탐색방향
countlist = [
    0,
    ((0,), (1,), (2,), (3,)),
    ((0,2), (1,3)),
    ((0,1), (1,2), (2,3), (3,0)),
    ((0,1,2), (1,2,3), (2,3,0), (3,0,1)),
    ((0,1,2,3),)
    ]

def cctvSearch(c, d, board):
    row, col = (c[0]+d[0], c[1]+d[1])
    while all((row >= 0, row < N, col >= 0, col < M)):
        if board[row][col] == 6:
            return None
        elif board[row][col] == 0:
            board[row][col] = 9
        row += d[0]
        col += d[1]

def searchCase(searchlist): #searchlist = ((coordinate), direction index), ...)
    res = 0
    newboard = deepcopy(originalboard)
    for cases in searchlist:
        num = newboard[cases[0][0]][cases[0][1]]
        for d in countlist[num][cases[1]]:
            cctvSearch(cases[0], direction[d], newboard)
    for row in newboard:
        res += row.count(0)
    return (res, newboard)

N, M = map(int, input().split())
originalboard = []
search = []
firstsearch = []
for r in range(N):
    row = list(map(int, input().split()))
    originalboard.append(row)
    for c, elem in enumerate(row):
        if elem > 0 and elem < 5:
            search.append(((r, c), elem))
        elif elem == 5:
            firstsearch.append((r,c))

for elem in firstsearch:
    for d in range(4):
        cctvSearch(elem, direction[d], originalboard)

# make case
# search: [((2, 2), 1), ((4, 4), 1)]
totalcount = 1
for s in search:
    totalcount *= len(countlist[s[1]])

targetCase = []
dindex = []
temp = [0] * len(search)
for eachcase in range(totalcount):
    for i in range(len(search)):
        temp[i] += 1
        if temp[i] == len(countlist[search[i][1]]):
            temp[i] = 0
            continue
        else:
            break
    dindex.append(deepcopy(temp))

minRes = 100
for d in dindex:
    slist = []
    for i in range(len(search)):
        newCase = (search[i][0], d[i])
        slist.append(newCase)
    comp, board = searchCase(slist)
    if minRes > comp:
        minRes = comp

print(minRes)