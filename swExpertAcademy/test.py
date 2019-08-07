from collections import deque

d = deque([1])


print(d)

for i in range(1):
    d[i] += 10
print(d)