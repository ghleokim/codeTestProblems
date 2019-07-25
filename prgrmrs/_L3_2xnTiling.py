# https://programmers.co.kr/learn/courses/30/lessons/12900
# 가로가 2이고 세로가 1인 직사각형 모양의 타일
# 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우기.
# 1 타일을 가로로 배치하는 경우 / 2 타일을 세로로 배치하는 경우
# 

# 2 2       = 4
# 1 1 1 1
# 1 1 2
# 2 1 1
# 1 2 1

# 1로 전부 채우는 경우
# 1이 두개씩 줄어들면서 채우는 경우
# 가로길이가 짝수일 경우 경우의 수 
# 2n개일 때 : m
# 2n+1개일 때 : 
# 홀수일 때는 가로길이 짝수일경우 + 1 하나 추가: 


n = 10

# 1 n개
result = []
case = []
for i in range(int(n/2)):
    case.append(['1']*(n-i))
for j in range(int(n/2)):
    case[j].extend(['2']*j)

print(case)

[]1[]1[]1[]1[]

# 1 n개     2 0개 ==== 1
# 1 n-2개   2 1개 ==== (n-2 + 1)C 1
# 1 n-4개   2 2개 ==== (n-4 + 1)C 2

# 1 1개(홀수) 2 (n-1)/2개 ==== 1

#combination:
# nCm = n * n - 1 * ... * n - m + 1 / m!

