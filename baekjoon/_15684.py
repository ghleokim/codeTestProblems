# https://www.acmicpc.net/problem/15684
"""
"""
#N개의 세로선과 M개의 가로선
#2차 배열로 정리


"""
import timeit
start = timeit.default_timer()


from pprint import pprint
from copy import deepcopy
from itertools import combinations

N, M, H = map(int, input().split())
ladder = [[0] * H for i in range(N)]
ladder2 = {}
for i in range(N):
    ladder2[i] = []

print(ladder2)
for _ in range(M):
    row, col = map(int, input().split())
    ladder2[col-1].append(row-1)
    ladder[col-1][row-1] = _+1
    if row < N:
        ladder[col][row-1] = (_+1)*-1

print(ladder2)

def ladder2Follow(num):
    c = 0
    while c < H:
        if num < N and c in ladder2[num]:
            num += 1
        elif num > 0 and c in ladder2[num-1]:
            num -= 1
        c += 1
    
    return num

def ladderFollow(num, ladder):
    c = 0
    while c < H:
        if num < N and ladder[num][c] > 0:
            num += 1
        elif num > 0 and ladder[num-1][c] > 0:
            num -= 1
        c += 1
    return num

pprint(ladder)
print('ladder test 1')
for i in range(N):

    print(i, ladderFollow(i, ladder))

print()
print('ladder test 2')

for i in range(N):
    print(i, ladder2Follow(i))

print()

def DFS(): # 다음 차례로 가지고 갈 것을 지정




"""
# pprint(ladder)
# for i in range(N):
#     print(i+1, ladderFollow(i, ladder)+1)
"""
targets = []

# 빈 공간
for i in range(N-1):
    for j in range(H):
        if not ladder[i][j] and not ladder[i+1][j]:
            targets.append((i,j))

result = 0

found = True
# check 0
for i in range(N):
    if i != ladderFollow(i, ladder):
        found = False

# check 1 ~ 3
if not found:
    for tests in range(1,4):
        for cases in combinations(targets,tests):
            nextCase = False
            for i in range(len(cases)-1):
                # 가로선 연속 걸러내기
                if cases[i][0] + 1 == cases[i+1][0] and cases[i][1] == cases[i+1][1]:
                    nextCase = True
            if nextCase:
                continue
            newladder = deepcopy(ladder)
            found = True
            
            for c in cases:
                if any((newladder[c[0]][c[1]], newladder[c[0]+1][c[1]])):
                    nextCase = True
                    break
                newladder[c[0]][c[1]] = 1
                newladder[c[0]+1][c[1]] = -1

            if nextCase:
                continue

            for i in range(N):
                # print('         ', end='')
                # print(i+1, ladderFollow(i, newladder)+1)
                if i != ladderFollow(i, newladder):
                    found = False
                    break
            # print(found)
            if found:
                result = tests
                break
        if found:
            break

if found:
    print(result)
else:
    print(-1)


stop = timeit.default_timer()
print(stop-start)

"""

from copy import deepcopy
from itertools import combinations

N, M, H = map(int, input().split())
ladder = {}
for i in range(N):
    ladder[i] = []
for _ in range(M):
    row, col = map(int, input().split())
    ladder[col-1].append(row-1)

def ladderFollow(num, ladder):
    c = 0
    while c < H:
        if num < N and c in ladder[num]:
            num += 1
        elif num > 0 and c in ladder[num-1]:
            num -= 1
        c += 1
    return num

targets = []
# 빈 공간 중 n개
for i in range(N-1):
    for j in range(H):
        if j not in ladder[i] and j not in ladder[i+1]:
            targets.append((i,j))

result = 0

found = True
# check 0
for i in range(N):
    if i != ladderFollow(i, ladder):
        found = False

# check 1 ~ 3
if not found:
    for tests in range(1,4):
        for cases in combinations(targets,tests):
            nextCase = False
            for i in range(len(cases)-1):
                # 가로선 연속 걸러내기
                if cases[i][0] + 1 == cases[i+1][0] and cases[i][1] == cases[i+1][1]:
                    nextCase = True
            if nextCase:
                continue
            newladder = deepcopy(ladder)
            found = True
            
            for c in cases:
                # if any((newladder[c[0]] == [c[1]], newladder[c[0]+1][c[1]])):
                #     nextCase = True
                #     break
                newladder[c[0]].append(c[1])

            for i in range(N):
                if i != ladderFollow(i, newladder):
                    found = False
                    break
            if found:
                result = tests
                break
        if found:
            break

if found:
    print(result)
else:
    print(-1)