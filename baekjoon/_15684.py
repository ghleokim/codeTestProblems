# https://www.acmicpc.net/problem/15684

"""
#N개의 세로선과 M개의 가로선
#2차 배열로 정리
"""

from pprint import pprint

N, M, H = map(int, input().split())
global ladder
global case

ladder = {}
case = None

for i in range(N):
    ladder[i] = [0] * H
for _ in range(M):
    row, col = map(int, input().split())
    ladder[col-1][row-1] = 1

def ladderFollow(num):
    global case
    c = 0
    if case:
        while c < H:
            if num == N:
                if (num-1, c) in case or ladder[num-1][c]:
                    num -= 1
            elif num == 0:
                if (num, c) in case or ladder[num][c]:
                    num += 1
            else:
                if (num, c) in case or ladder[num][c]:
                    num += 1
                elif (num-1, c) in case or ladder[num-1][c]:
                    num -= 1
            c += 1
    else:
        while c < H:
            if num == N:
                if ladder[num-1][c]:
                    num -= 1
            elif num == 0:
                if ladder[num][c]:
                    num += 1
            else:
                if ladder[num][c]:
                    num += 1
                elif ladder[num-1][c]:
                    num -= 1
            c += 1
    return num

targets = []

# 빈 공간 만들기
for i in range(N-1):
    for j in range(H):
        if not ladder[i][j]:
            if i > 0:
                if ladder[i-1][j]: continue
            if ladder[i+1][j]: continue
            targets.append((i,j))

def dfs(targets, k, visited=[]): # targets: 전체 대상, k: 필요한 depth, visited: 현재까지 방문한 것
    if len(visited) == k:
        yield visited
    else:
        for i in range(len(targets)):
            if (targets[i][0]-1, targets[i][1]) in visited:
                continue
            elif (targets[i][0]+1, targets[i][1]) in visited:
                continue
            visited.append(targets[i])
            yield from dfs(targets[i+1:], k, visited)
            visited.pop()

# 탐색
result = 0
found = False
if M % 2:
    # 홀수이면 1, 3 탐색
    if not found:
        for tests in [1,3]:
            for c in dfs(targets, tests):
                case = c
                for i in range(N):
                    if i != ladderFollow(i):
                        break
                else:
                    found = True
                    result = tests
                    break
                del case
            if found:
                break
else:
    # 짝수이면 0, 2 탐색
    found=True

    # check 0
    for i in range(N):
        case = []
        if i != ladderFollow(i):
            found = False
    # check 2
    if not found:
        tests = 2
        for c in dfs(targets, tests):
            case = c
            for i in range(N):
                if i != ladderFollow(i):
                    break
            else:
                result = tests
                found = True
                break
            del case

# 출력
if found:
    print(result)
else:
    print(-1)



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
            elif num == 0:
                if (num, c) in case or c in ladder[num]:
                    num += 1
            else:
                if (num, c) in case or c in ladder[num]:
                    num += 1
                elif (num-1, c) in case or c in ladder[num-1]:
                    num -= 1
            c += 1
    else:
        while c < H:
            if num == N:
                if c in ladder[num-1]:
                    num -= 1
            elif num == 0:
                if c in ladder[num]:
                    num += 1
            else:
                if c in ladder[num]:
                    num += 1
                elif c in ladder[num-1]:
                    num -= 1
            c += 1
    return num

targets = []

# 빈 공간 만들기
for i in range(N-1):
    for j in range(H):
        if j not in ladder[i]:
            if i > 0:
                if j in ladder[i-1]: continue
            if j in ladder[i+1]: continue
            targets.append((i,j))

def dfs(targets, k, visited=[]): # targets: 전체 대상, k: 필요한 depth, visited: 현재까지 방문한 것
    if len(visited) == k:
        yield visited
    else:
        for i in range(len(targets)):
            if (targets[i][0]-1, targets[i][1]) in visited:
                continue
            elif (targets[i][0]+1, targets[i][1]) in visited:
                continue
            visited.append(targets[i])
            yield from dfs(targets[i+1:], k, visited)
            visited.pop()

# 탐색
result = 0
found = False
if M % 2:
    # 홀수이면 1, 3 탐색
    if not found:
        for tests in [1,3]:
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
    # check 2
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

# 출력
if found:
    print(result)
else:
    print(-1)


"""