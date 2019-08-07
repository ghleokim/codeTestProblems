for i in range(int(input())):
    a = input().split()
    a.remove(max(a))
    a.remove(min(a))

    res=round(sum(a) / len(a))
    print(f'#{i+1} {res}')