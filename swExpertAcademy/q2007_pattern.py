case = int(input())

for num in range(1,case+1):
    st = input()
    res = 1
    while res<=10:
        if st[:res] == st[res:res*2]:
            break
        # test = st[:res]
        # test2 = st[res:res*2]
        # print(test,test2)
        res+=1


    print('#{0} {1}'.format(num, res))
