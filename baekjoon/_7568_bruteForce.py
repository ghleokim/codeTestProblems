# https://www.acmicpc.net/problem/7568

people = []

N = int(input())

for _ in range(N):
    people.append(tuple(map(int,input().split())))

print(people)

rank = [0] * N

for number, person in enumerate(people):
    # get former list
    former = people[:number]
    print(number, former)
    if not former:
        rank[0] = 1
        continue

    # n명의 사람이 있을 때 k등이 될 경우:
    # 등수 같은 사람 카운트(본인 포함)
    # k보다 큰 등수 전부 미루기
    newR = rank[0]
    cntSame = 1

    for fnum, fper in enumerate(former):
        print('     fnum', end=' ')
        print(fnum)
        print(newR)
        
        if fper[0] > person[0] and fper[1] > person[1]:
            if newR > rank[fnum]:
                newR = rank[fnum] - 1 

        elif fper[0] < person[0] and fper[1] < person[1]:
            if newR < rank[fnum]:
                newR = rank[fnum] + 1
        else:
            newR = rank[fnum]
            cntSame += 1
            print('cntSame', end=' ')
            print(cntSame)
    print(rank)
    
    for fnum in range(len(former)):
        if newR == 1:
            rank[fnum] += cntSame
        elif rank[fnum] > newR:
            rank[fnum] += cntSame

    rank[number] = newR



print(rank)






"""
    # compare
    for num, frmr in enumerate(former):
        # new bigger
        if person[0] > frmr[0] and person[1] > frmr[1]:
            print('case A:::')
            if newR != 1:
                newR -= 1
            for i in range(number-1):
                if rank[i] >= newR:
                    rank[i] += 1

        # new smaller
        elif person[0] < frmr[0] and person[1] < frmr[1]:
            print('case B:::')
            newR += 1

        # cannot compare
        else:
            print('case C:::')
        
        print(newR)
    
    for num, frmr in enumerate(former):
        if rank[num] > newR:
            rank[num] += 1
    
    rank[number] = newR
    print(rank)
        
print(rank)
"""