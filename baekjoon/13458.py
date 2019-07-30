# N개의 시험장
# i번 시험장 응시자 A_i명
# 총감독관 응시자 수 B
# 부감독관 응시자 수 C

import math

# n = int(input())
# ai = list(map(int,input().split()))
# bc = list(map(int,input().split()))

n = 5
ai = [10, 9, 10, 9, 10]
bc = [7,20]


print(n + sum(math.ceil((item-bc[0])/bc[1]) for item in ai))



# for num in range(n):
#     ai[num] -= bc[0]
#     if ai[num] < 0:
#         ai[num]=0
#         continue
#     elif ai[num] - int(ai[num]):
#         ai[num] = int(ai[num]) + 1

#     q, r = ai[num] // bc[1], ai[num] % bc[1]
#     if r > 0:
#         ai[num] = q + 1
#     else:
#         ai[num] = q

# res += sum(ai) + n

# print(res)