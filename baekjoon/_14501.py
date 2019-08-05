#https://www.acmicpc.net/problem/14501

#상담 일자는 set으로 접근.

# t = [3,5,1,1,2,4,2]
# p = [10,20,10,20,15,40,200]

t, p = [],[]
for N in range(int(input())):
    temp=list(map(int, input().split()))
    t.append(temp[0])
    p.append(temp[1])

n=len(t)

visited = [0] * len(t)

timetable = []

def makeSet(idx, currentSet):
    if idx + t[idx] > len(t):
        timetable.append(currentSet)
    else:
        visited[idx]=1
        currentSet.add(idx)
        #탐색, 다음 노드 검색
        for i in range(idx+t[idx],n):
            if visited[i]==1:
                continue
            else:
                makeSet(i,currentSet)
        
for i in range(len(t)):
    makeSet(i,set())

result = []

for sets in timetable:
    res=0
    for i in sets:
        res += p[i]
    result.append(res)

print(max(result))