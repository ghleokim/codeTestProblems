# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
c = list(map(int, input().split()))
res = []
for i in range(len(c)):
    for j in range(i):
        for k in range(j):
            res.append(c[i]+c[j]+c[k])
for item in sorted(res)[::-1]:
    if item <= m:
        print(item)
        break