# alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# for a in alpha:
#     num = list(map(ord,list(a)))
#     for n in num:
#         print(n-65, end= ' ')
#     print()
"""
0 1 2 
3 4 5 
6 7 8 
9 10 11 
12 13 14 
15 16 17 18 
19 20 21 
22 23 24 25 
"""

# ordList = [0, 3, 6, 9, 12, 15, 19, 22]
ordList = [2, 5, 8, 11, 14, 18, 21, 25]

# ordList = ['A', 'D', 'G', 'J', 'M', 'P', 'T', 'W']

txt = list(input())

res = 0

for t in txt:
    for en, al in enumerate(ordList):
        if ord(t) - 65 > al:
            continue
        else:
            print(en + 2, t)
            res += en + 2 + 1
            break

print(res)
#ABCDEFGHIJKLMNOPQRSTUVWXYZ