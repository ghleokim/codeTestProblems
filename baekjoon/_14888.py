# https://www.acmicpc.net/problem/14888

"""
연산자 끼워넣기

n개의 수로 이루어진 수열 a1,a2,...,an

n-1개의 연산자: + - * /

연산자 우선순위 무시

음수로 양수를 나눌 때는 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꾼다.
양수 / 음수 = 양수 // -음수 * -1

"""

import itertools

N = int(input())
a = list(map(int, input().split()))
calc = list(map(int, input().split()))

s = ''

for en, num in enumerate(calc):
    s += str(en)*num

max = 0
min = 0

for cases in itertools.permutations(s, N-1):
    res = 0
    for en, num in enumerate(a):
        print(en)
        if en == len(a)-1:
            break
        else:
            if cases[en] == '0':
                res += a[en]
            elif cases[en] == '1':
                res -= a[en]
            elif cases[en] == '2':
                res *= a[en]
            else:
                res /= a[en]
    print(res)
