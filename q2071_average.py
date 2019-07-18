# 평균값 구하기
# 테스트케이스 개수 T, 그 뒤로 10개의 숫자가 T줄만큼 입력됨.
# input example)
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   

# output example)
# #1 24
# #2 29
# #3 27

num = int(input())

for enum in range(1,num+1):
    c = input().split(' ')
    if c[-1] == '':
        c.pop(-1)
    
    
    print('#{0} {1}'.format(enum, round(sum(map(int, c))/len(c))))