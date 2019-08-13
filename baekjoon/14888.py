# 20190813_백준_14888.py
# https://www.acmicpc.net/problem/14888

"""
연산자 끼워넣기

n개의 수로 이루어진 수열 a1,a2,...,an

n-1개의 연산자: + - * /

연산자 우선순위 무시

음수로 양수를 나눌 때는 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꾼다.
양수 / 음수 = 양수 // -음수 * -1

117804kb
1148ms
"""

import itertools

N = int(input())
a = list(map(int, input().split()))
calc = list(map(int, input().split()))

s = ''

for en, num in enumerate(calc):
    s += str(en)*num

maxRes, minRes = None, None

for cases in itertools.permutations(s, N-1):
    res = 0
    for en, num in enumerate(a):
        if en == len(a):
            break
        elif en == 0:
            res = a[en]
        else:
            if cases[en-1] == '0':
                res += a[en]
            elif cases[en-1] == '1':
                res -= a[en]
            elif cases[en-1] == '2':
                res *= a[en]
            else:
                if res < 0:
                    tmp = abs(res) // a[en]
                    res = tmp * (-1)
                else:
                    tmp = res // a[en]
                    res = tmp
    if maxRes is None:
        maxRes = res
        minRes = res
    elif maxRes < res:
        maxRes = res
    elif minRes > res:
        minRes = res
    else:
        continue

print(maxRes)
print(minRes)


    