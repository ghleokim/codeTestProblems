# https://www.acmicpc.net/problem/2231

n = int(input())

for number in range(1,n+1):
    # sum과 map을 이용하면 더 빠르다.
    # compare = number + sum(map(int, str(number)))

    compare = number 
    for digit in str(number):
        compare += int(digit)
    if compare == n:
        print(number)
        break
else:
    print(0)