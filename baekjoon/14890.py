# 20190813_백준_14890.py
# https://www.acmicpc.net/problem/14890
"""
크기 N*N인 지도. 각 칸에는 높이.
지나갈 수 있는 길의 갯수 구하기

경사로 길이 L, 높이 항상 1

1 1 1 2, 경사로 L: 1 (1 1) 2로 경사로 설치 가능
"""

from collections import deque

def checkPath(path):
    d_path = deque(path)
    order = [deque.popleft(d_path)]
    counts = [1]

    for _ in range(N-1):
        diff = abs(order[-1] - d_path[0])
        if diff > 1:
            return False
        elif diff == 1:
            order.append(deque.popleft(d_path))
            counts.append(1)
        else:
            deque.popleft(d_path)
            counts[-1] += 1
    
    print('     order: {} | counts: {}'.format(order, counts))

    for num, height in enumerate(order):
        if num == len(order) - 1:
            return True
        else:
            nextHeight = order[num + 1]
            if height > nextHeight:
                counts[num + 1] -= L
                if counts[num + 1] < 0:
                    return False
            else:
                counts[num] -= L
                if counts[num] < 0:
                    return False

    return 0


from pprint import pprint

N, L = map(int, input().split())

board = []

for row in range(N):
    board.append([*map(int, input().split())])

pprint(board)

cnt = 0
# 가로
for row in board:
    print('cnt {}'.format(cnt))
    print(row, set(row))
    if len(set(row)) == 1:
        cnt += 1
        continue
    elif checkPath(row):
        cnt += 1
    print('     {}'.format(checkPath(row)))

for col in zip(*board):
    print(col, set(col))
    if len(set(col)) == 1:
        cnt += 1
        continue
    elif checkPath(col):
        cnt += 1
    print('     {}'.format(checkPath(col)))

print(cnt)
