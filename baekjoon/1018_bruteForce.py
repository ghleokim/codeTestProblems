# https://www.acmicpc.net/problem/1018

"""
8*8 타일이 정해진 이후
B first or W first?
B first일 때 타일
W first일 때 타일

둘 중 최소값 저장
"""

# a = 'abc'
# b = 'abb'
# c = sum(map(lambda x: int(*map(lambda y, z: 1 if y == z else 0, *x)), zip(a,b)))

refs = ('BWBWBWBW', 'WBWBWBWB')

def compare(tar, row):
    compA = sum(map(lambda x: int(*map(lambda y, z: 1 if y == z else 0, *x)), zip(tar, refs[0])))
    compB = sum(map(lambda x: int(*map(lambda y, z: 1 if y == z else 0, *x)), zip(tar, refs[1])))
    if row % 2:
        return (compA, compB)
    else:
        return (compB, compA)

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(input())

result = 64

for rowOffset in range(N-7):
    for colOffset in range(M-7):
        r = 0
        res = []
        for i in range(8):
            a = board[i+rowOffset][colOffset:colOffset+8]
            res.append(compare(a, i))
        r = min(map(sum, zip(*res)))
        if r < result:
            result = r

print(result)