# [0,0,0,0]
# ['','','','']
# [' ',' ',' ',' ']

# for case in case_list:
#     show = [['','','',''],['','','',''],['','','',''],['','','','']]
#     for n in range(4):
#         show[case[n][1]][case[n][0]] = n+1

#     for i in show:
#         print(i)
#     print('----')


case_list = [
    # 4 * 1
    [(0,0),(1,0),(2,0),(3,0)],  # 0 ㅡ

    # 3 * 2
    [(0,0),(1,0),(2,0),(2,1)],  # 1 ㄱ
    [(0,0),(0,1),(1,1),(2,1)],  # 2 ㄴ
    [(0,1),(0,0),(1,0),(2,0)],  # 3 ㄱ대칭
    [(0,1),(1,1),(2,1),(2,0)],  # 4 ㄴ대칭
    [(0,0),(1,0),(1,1),(2,1)],  # 5 ㄱㄴ
    [(0,1),(1,1),(1,0),(2,0)],  # 6 ㄱㄴ 대칭
    [(0,0),(1,0),(2,0),(1,1)],  # 7 ㅜ
    [(0,1),(1,1),(1,0),(2,1)],  # 8 ㅗ

    # 2 * 2
    [(0,0),(1,0),(0,1),(1,1)],  # 9 ㅁ
    # 2 * 3
    [(0,0),(1,0),(1,1),(1,2)],  # 10 ㄱ
    [(0,0),(0,1),(0,2),(1,2)],  # 11 ㄴ
    [(1,0),(0,0),(0,1),(0,2)],  # 12 ㄱ대칭
    [(1,0),(1,1),(1,2),(0,2)],  # 13 ㄴ대칭
    [(0,0),(0,1),(1,1),(1,2)],  # 14 ㄴㄱ
    [(1,0),(1,1),(0,1),(0,2)],  # 15 ㄴㄱ대칭
    [(0,0),(0,1),(0,2),(1,1)],  # 16 ㅏ
    [(1,0),(1,1),(1,2),(0,1)],  # 17 ㅓ

    # 1 * 4
    [(0,0),(0,1),(0,2),(0,3)]  # 18 ㅣ
]

# pos: x, y, m, n
def getSum(cases, pos):
    res = 0
    for box in cases:
        i = box[0] + pos[0]
        j = box[1] + pos[1]
        res += board[j][i]

    return res

def getCase(pos):
    res = []
    for cases in case_list:
        try:
            res.append(getSum(cases,pos))
        except IndexError:
            continue
    if not res:
        return 0
    else:
        return max(res)


n, m = map(int, input().split())

board = []
for row in range(n):
    board.append(list(map(int, input().split())))

result = []
for xPos in range(m):
    for yPos in range(n):
        result.append(getCase((xPos, yPos, m, n)))

print(max(result))

