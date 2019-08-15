# https://www.acmicpc.net/problem/1436

"""
666부터 10000까지의 숫자 중 N번째로 666이 연속으로 들어간 수 구하기
"""
num = 666
cnt = 1
N = int(input())

while True:
    if N == cnt or num > 10000:
        print(num)
        break
    
    num += 1
    if '666' in str(num):
        cnt += 1
    
    