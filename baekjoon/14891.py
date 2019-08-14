# 20190814_백준_14891.py
# https://www.acmicpc.net/problem/14891

"""
총 8개의 톱니를 가진 톱니바퀴 4개
각 톱니의 방향 리스트: 현재 12시방향에 있는 톱니의 인덱스 = [g1, g2, g3, g4]

시계방향 회전: g - 1,
반시계방향 회전: g + 1

3시방향: (g + 2) % 8
9시방향: (g + 6) % 8

"""
"""
gear = [15,16,17,18,19,25,26,27,28,29]

# n번째 톱니바퀴(i=n-1)부터 1번째 톱니바퀴(i=0)까지
# 아래가 더 빠르다.
i = 6
for g in range(i,-1,-1):
    print(g, gear[g])
for g in gear[i::-1]:
    print(g)

# n번째 톱니바퀴(i=n-1)부터 끝까지
for g in gear[i:]:
    print(g)

# ---- #
"""
gear = []
for _ in range(4):
    gear.append(input())

tooth_12 = [0,0,0,0]

for K in range(int(input())):
    target, direction = map(int, input().split())
    target -= 1

    # n부터 첫번째까지
    rotation = [0] * 4

    for offset, g in enumerate(gear[target::-1]):
        if offset == target:
            break

        # 회전방향 세팅
        if offset % 2:
            currentDir = direction
        else:
            currentDir = direction * -1

        rotation[target-offset] = currentDir

        # 현재 기어의 3시방향
        current = (tooth_12[target-offset] + 6) % 8
        # 이전 기어의 9시방향
        former = (tooth_12[target-offset-1] + 2) % 8
        
        if g[current] == gear[target-offset-1][former]:
            break
        else:
            rotation[target-offset-1] = currentDir * -1

    for offset, g in enumerate(gear[target:]):
        print('offset, g = {}, {}'.format(offset, g))
        if offset == 3-target:
            break

        # 회전방향 세팅
        if offset % 2:
            currentDir = direction
        else:
            currentDir = direction * -1
        
        rotation[target+offset] = currentDir

        # 현재 기어의 9시방향
        current = (tooth_12[target+offset] + 2) % 8
        # 다음 기어의 3시방향
        latter = (tooth_12[target+offset+1] + 6) % 8
        
        if g[current] == gear[target+offset+1][latter]:
            break
        else:
            rotation[target+offset+1] = currentDir * -1

    tmp = [0]*4
    for i in range(4):
        tmp[i] = (tooth_12[i]+rotation[i]) % 8
    tooth_12 = tmp

result = 0
for num, g in enumerate(gear):
    if g[tooth_12[num]] == '1':
        print(2 ** num, num, g[tooth_12[num]])
        result += 2 ** num

print(result)
        