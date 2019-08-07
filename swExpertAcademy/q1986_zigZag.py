for i in range(int(input())):
    res=0
    for j in range(1,int(input())+1):
        res += (j if j % 2 else -j)
    print(f'#{i+1} {res}')

