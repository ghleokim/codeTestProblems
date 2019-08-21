global ladder
global case

N, M, H = map(int, input().split())
ladder = {}
case = None

for i in range(N):
    ladder[i] = [0] * H
for _ in range(M):
    row, col = map(int, input().split())
    ladder[col-1][row-1] = 1

print(ladder)

def checkladder():
    global ladder
    row = 0
    move_left = False
    move_right = False

    for i in range(N):
        col = i
        while row < H:
            if col == 0:
                if ladder[col][row]:
                    move_right = True

            elif col == N:
                if ladder[col-1][row]:
                    
            else:





            if move_left:
                col -= 1
            elif move_right:
                col += 1
            else:
                continue

        

    return True

checkladder(i)

"""
# 출력
if found:
    print(result)
else:
    print(-1)
"""