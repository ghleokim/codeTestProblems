# 20190813_백준_14889.py
# https://www.acmicpc.net/problem/14889
"""
N(짝수)명의 사람.
s[i][j]-i번과 j번이 같은 팀에 속했을 때 팀에 더해지는 능력치

N/2명을 고르면 나머지는 자동으로 구해진다.
2진법으로 powerset 계산해보기
"""

from pprint import pprint

N = int(input())

skill = []

for row in range(N):
    skill.append([*map(int, input().split())])

pprint(skill)

choicesA = []
choicesB = []

for i in range(1 << N):
    resA, resB = [], []
    for j in range(N):
        if i & (1 << j):
            resA.append(j)
        else:
            resB.append(j)
    # N/2개인 것들만 가르기
    if len(resA) == N//2:
        choicesA.append(resA)
        choicesB.append(resB)

# combination으로 하는 것이 나을 듯

print(choicesA, choicesB)
        
result = None

for cnt in range(len(choicesA)):
    A, B = 0, 0
    cA, cB = choicesA[cnt], choicesB[cnt]
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            A += skill[cA[i]][cA[j]] + skill[cA[j]][cA[i]]
            B += skill[cB[i]][cB[j]] + skill[cB[j]][cB[i]]
    print(A, B)
    tmp = abs(A-B)
    if result is None:
        result = tmp
    elif result > tmp:
        result = tmp
    else:
        continue

print(result)

# -------------------------- #

from pprint import pprint
from itertools import combinations

N = int(input())

skill = []

for row in range(N):
    skill.append([*map(int, input().split())])

# combaination
comb = {*combinations(range(N), N // 2)}

choices = []

for A in comb:
    B = set(range(N)).difference(A)
    choices.append((A,tuple(B)))

result = None

for choice in choices:
    teamA, teamB = 0, 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            teamA += skill[choice[0][i]][choice[0][j]] + skill[choice[0][j]][choice[0][i]]
            teamB += skill[choice[1][i]][choice[1][j]] + skill[choice[1][j]][choice[1][i]]
    tmp = abs(teamA - teamB)
    if result is None:
        result = tmp
    elif result > tmp:
        result = tmp
    else:
        continue

print(result)
