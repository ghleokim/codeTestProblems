# https://www.acmicpc.net/problem/15684

"""
#N개의 세로선과 M개의 가로선
#2차 배열로 정리
"""

from pprint import pprint

N, M, H = map(int, input().split())
ladder = {}

for i in range(N):
    ladder[i] = []
for _ in range(M):
    row, col = map(int, input().split())
    ladder[col-1].append(row-1)

def ladderFollow(num, case=None):
    c = 0
    if case:
        while c < H:
            if num == N:
                if (num-1, c) in case or c in ladder[num-1]:
                    num -= 1
                c += 1
                continue
            elif num == 0:
                if (num, c) in case or c in ladder[num]:
                    num += 1
                c += 1
                continue
            else:
                if (num, c) in case or c in ladder[num]:
                    num += 1
                elif (num-1, c) in case or c in ladder[num-1]:
                    num -= 1
                c += 1
                continue

            # if (num, c) in case:
            #     num += 1
            #     c += 1
            #     continue
            # elif num < N and c in ladder[num]:
            #     num += 1
            #     c += 1
            #     continue
            # elif num > 0 and (num - 1, c) in case:
            #     num -= 1
            #     c += 1
            #     continue
            # elif num > 0 and c in ladder[num-1]:
            #     num -= 1
            #     c += 1
            #     continue
            c += 1
    else:
        while c < H:
            if num == N:
                if c in ladder[num-1]:
                    num -= 1
                c += 1
                continue
            elif num == 0:
                if c in ladder[num]:
                    num += 1
                c += 1
                continue
            else:
                if c in ladder[num]:
                    num += 1
                elif c in ladder[num-1]:
                    num -= 1
                c += 1
                continue
            # if num < N and c in ladder[num]:
            #     num += 1
            # elif num > 0 and c in ladder[num-1]:
            #     num -= 1
            # c += 1
    return num

targets = []

# 빈 공간
for i in range(N-1):
    for j in range(H):
        if j not in ladder[i]:
            targets.append((i,j))

def dfs(targets, k, visited=[]): # targets: 전체 대상, k: 필요한 depth, visited: 현재까지 방문한 것
    if len(visited) == k:
        yield visited
    else:
        for i in range(len(targets)):
            if (targets[i][0]-1, targets[i][1]) in visited:
                continue
            visited.append(targets[i])
            yield from dfs(targets[i+1:], k, visited)
            visited.pop()

result = 0

found = False

if M % 2:
    # 홀수이면 1, 3 탐색
    if not found:
        for tests in range(1,4,2):
            for case in dfs(targets, tests):
                for i in range(N):
                    if i != ladderFollow(i, case):
                        break
                else:
                    found = True
                    result = tests
                    break
            if found:
                break

else:
    # 짝수이면 0, 2 탐색
    found=True
    # check 0
    for i in range(N):
        if i != ladderFollow(i):
            found = False

    if not found:
        tests = 2
        for case in dfs(targets, tests):
            for i in range(N):
                if i != ladderFollow(i, case):
                    break
            else:
                result = tests
                found = True
                break

if found:
    print(result)
else:
    print(-1)



"""

if M % 2:
    # 홀수이면 1, 3 탐색
    if not found:
        for tests in range(1,4,2):
            for case in dfs(targets, tests):
                found = True
                for i in range(N):
                    if i != ladderFollow(i, ladder, case):
                        found = False
                        break
                if found:
                    result = tests
                    break
            if found:
                break

else:
    # 짝수이면 0, 2 탐색
    # check 0
    for i in range(N):
        if i != ladderFollow(i, ladder):
            found = False

    if not found:
        tests = 2
        for case in dfs(targets, tests):
            found = True
            for i in range(N):
                if i != ladderFollow(i, ladder, case):
                    found = False
                    break
            if found:
                result = tests
                break

"""