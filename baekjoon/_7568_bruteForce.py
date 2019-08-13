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

    newR = rank[0]

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