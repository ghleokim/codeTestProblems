# https://www.acmicpc.net/problem/15686

"""
# 시간초과
from itertools import combinations

N, M = map(int,input().split())
board = [[0 for _ in range(N)] for __ in range(N)]
house = []
chicken = []
for i in range(N):
    tmp = [*map(int,input().split())]
    for j in range(N):
        if tmp[j] == 1:
            house.append((i,j))
            board[i][j]=tmp[j]
        elif tmp[j] == 2: chicken.append((i,j))

#     E  S  W  N
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def checkBoundary(r, c):
    if any((r<0,c<0,r==N,c==N)): return False
    return True

def bfs(r, c):
    depth = 0
    queue = []
    queue.append((r,c,depth))
    visited[r][c] = 1

    while queue:
        ri, ci, dp = queue[0]
        depth = dp + 1
        del queue[0]
        for i in range(4):
            nr = ri + dr[i]
            nc = ci + dc[i]
            if checkBoundary(nr,nc):
                if board[nr][nc]==2:
                    return depth
                elif not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr,nc,depth))
    return 0

min_distance = 1500

for case in combinations(chicken, M):
    dist = 0
    for c in case:
        board[c[0]][c[1]] = 2

    for h in house:
        visited = [[0 for _ in range(N)] for __ in range(N)]
        dist += bfs(h[0],h[1])

    if dist < min_distance:
        min_distance = dist

    for c in case:
        board[c[0]][c[1]] = 0

print(min_distance)
"""
# 118100 kb | 164 ms
from itertools import combinations

N, M = map(int,input().split())
house = []
chicken = []
for i in range(N):
    tmp = [*map(int,input().split())]
    for j in range(N):
        if tmp[j] == 1: house.append((i,j))
        elif tmp[j] == 2: chicken.append((i,j))

min_distance = 1500

for case in combinations(chicken, M):
    dist = 0
    for x, y in house:
        tmp = 150
        for r, c in case:
            t = abs(x-r) + abs(y-c)
            if t < tmp:
                tmp = t
        dist += tmp
    if dist < min_distance:
        min_distance = dist

print(min_distance)