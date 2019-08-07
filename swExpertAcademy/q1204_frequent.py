from collections import Counter

a = int(input())

for time in range(a):
    n, d = input(), input()

    li = d.split()

    result = Counter(li).most_common(1)[0][0]

    print(f'#{n} {result}')