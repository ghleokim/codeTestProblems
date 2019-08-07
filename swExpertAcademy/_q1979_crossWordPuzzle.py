# for i in range(int(input())):
#     n, k = input().split()
#     r = []
#     count = 0
#     for puzzleRow in range(int(n)):
#         r.append(input().split())
#     for elem in r:
#         if '0'*k in ''.join(elem):
#             count += 1
#     for elem in list(zip(r)):
#         if '0'*k in ''.join(elem):
#             count += 1
#     print(f'#{i} {count}')

for i in range(int(input())):
    n, k = input().split()
    r = []
    count = 0
    for puzzleRow in range(int(n)):
        r.append(input().split())
    for elem in r:
        if '0'*int(k) in ''.join(elem):
            count += 1
    for elem in list(zip(r))[0]:
        if '0'*int(k) in ''.join(elem):
            count += 1
    print(f'#{i} {count}')
