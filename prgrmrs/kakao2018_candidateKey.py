# candidate key

# relT = [*zip(*relation)]

target = [0,1,2,3,4,5]

visited = [1 for _ in range(6)]

# n개를 선택하고 해당 조합이 후보 키가 되는지 검사
n = 2


stack = []

for i in range(2**len(target)):
    tmp = []
    for j in range(len(target)):
        if (i >> j) % 2 == 1:
            tmp.append(j)
    if len(tmp) == 2:
        print(tmp)