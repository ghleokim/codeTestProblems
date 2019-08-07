for i in range(int(input())):
    (n,m) = map(int,input().split())
    case=[]
    for row in range(n):
        case.append(list(map(int,input().split())))
    res = []
    
    # m*m 사각형으로 줄이기
    #
    res2 = []
    for row in range(n):
        for col in range(n-m+1):
            res2.append(case[row][col]+case[row][col+1]+case[row][col+2])
    
    print(res2)