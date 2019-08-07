#n의 배수 양
#
ref = {'0','1','2','3','4','5','6','7','8','9'}

for i in range(int(input())):
    m = n = input()
    k = 1
    nset = set(n)

    while nset != ref:
        print(nset)
        print(m)
        m=str(int(m)+int(n))
        nset |= set(m)
        k+=1

    print(f'#{i+1} {m}')




