target = int(input())

numList = map(str, range(2,target+1))

print('1',end='')
for num in numList:
    print(' ',end='')
    num = num.replace('3','-')
    num = num.replace('6','-')
    num = num.replace('9','-')
    if not num.isdigit() and not num == '-' and not num == '--':
        num = '-'
    print(num,end='')