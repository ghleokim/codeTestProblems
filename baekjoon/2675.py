T = int(input())

for num in range(T):
    RS = input().split(' ')
    print(''.join(map(lambda x : x * int(RS[0]), RS[1])))