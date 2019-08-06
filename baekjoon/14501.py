#https://www.acmicpc.net/problem/14501
#상담 일자는 set으로 접근

n = int(input())
t, p = [],[]
for i in range(n):
    temp=list(map(int, input().split()))
    t.append(temp[0])
    p.append(temp[1])

timetable,result=[], []
visited = [0] * n

def makeSet(idx, previous, current):
    if idx+t[idx] > n:
        # print('out of range')
        if (not timetable) or (timetable[-1] != previous):
            timetable.append(previous)
    elif idx+t[idx] == n:
        current = previous | {idx}
        timetable.append(current)
    else:
        current = previous | {idx}
        # print(current)
        for i in range(idx+t[idx],n):
            makeSet(i, current, set())

for i in range(n):
    makeSet(i,set(),set())

for sets in timetable:
    res=0
    for i in sets:
        res += p[i]
    result.append(res)

print(timetable)
print(max(result))