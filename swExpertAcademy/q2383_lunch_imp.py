# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&

# 계단 list1, list2 []
# 사람 list: index = id, value = stair time
# time

from collections import deque
from pprint import pprint
import sys
sys.stdin = open('input/input2383.txt', 'r')

def getTime(stair, wait): # stair1, 2: 계단의 길이, wait1, 2: 대기열
    elev1 = deque() # 최대 3명
    w1 = deque(wait)
    
    finish = True
    clok = 0 # minute
    while finish:
        # print('   clock = {0}'.format(clok), end='  |  ')
        # people in elevator
        # check if people can get off
        pop1 = 0
        for p in elev1:
            if p < clok - stair:
                pop1 += 1
        for i in range(pop1):
            elev1.popleft()
        
        # 엘리베이터 탑승
        while len(elev1) < 3 and w1:
            if w1[0] <= clok:
                elev1.append(w1.popleft())
            else:
                break
        # stack full
        if len(elev1) == 3:
            for p in range(len(w1)):
                if w1[p]+1 == clok:
                    w1[p] += 1
        clok += 1
        
        # print('moving: ',end='')
        # print(elev1, elev2,end='  |  ')
        # print('wainting: ',end='')
        # print(w1, w2)

        if all((not elev1, not w1)):
            finish = False
        
            # print(clok - 1)
            # print('exit')
    
    return clok-1

for T in range(int(input())):
    i = int(input())
    data = []
    for j in range(i):
        data.append(list(map(int,input().split())))

    # 계단, 사람의 위치 찾기
    # 계단: (y좌표, x좌표, 길이)
    # 사람: (y좌표, x좌표)
    stair = []
    people = []
    for row in range(i):
        for col in range(i):
            if data[row][col] > 1:
                stair.append((row, col, data[row][col]))
            elif data[row][col] == 1:
                people.append((row,col))

    # print(stair, people)
            
    # 각 사람과 계단간의 거리 구하기
    dis1 = []
    dis2 = []

    for person in people:
        dis1.append(abs(person[0] - stair[0][0]) + abs(person[1] - stair[0][1]))
        dis2.append(abs(person[0] - stair[1][0]) + abs(person[1] - stair[1][1]))

    # print(dis1)
    # print(dis2)
    # print('---')

    res = []
    for i in range(1 << len(people)):   # 사람들이 계단을 선택하는 모든 부분집합을 구함
        w1, w2 = [], []
        for j in range(len(people)):
            if i & (1 << j): # 첫번째 계단으로 갈 때
                w1.append(dis1[j])
            else:   # 두번째 계단으로 갈 때
                w2.append(dis2[j])
        # print('stair: ',end='')
        # print(stair[0][2],stair[1][2])
        res.append(max(getTime(stair[0][2],sorted(w1)), getTime(stair[1][2], sorted(w2))))

    # pprint('wait1 : {0}'.format(wait1))
    # pprint('wait2 : {0}'.format(wait2))

    print(min(res))