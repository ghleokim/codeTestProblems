# candidate key

# relT = [*zip(*relation)]

target = [0,1,2,3,4,5]

visited = [1 for _ in range(6)]

# n개를 선택하고 해당 조합이 후보 키가 되는지 검사
# N개 중 M(1 ~ N)개를 선택, 만약 해당 조합 열이 최소성과 유일성을 동시에 만족한다면 후보키 대상.
# 만약 M개를 전부 탐색했을 때 후보키가 되는 조합이 여러 개인 경우는 모두 다음 대상에서 제외.
# 만약 M+1개보다 적은 후보가 다음 대상에 있다면 끝.

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

def comb(N, k, d=0, st=0,case=[]):
    if d == k:
        yield case
    for i in range(st, len(N)):
        case.append(N[i])
        yield from comb(N, k, d+1, i+1, case)
        case.pop()

def checkCandi(col):
    comp = [tuple(relation[i][c] for c in col) for i in range(len(relation))]
    if len(set(comp)) == len(comp): return True
    else: return False

print(checkCandi([1,3]))

# visited=[0 for _ in range(5)]

N = [i for i in range(len(relation[0]))]
M = 1
cnt = 0
while M <= len(N):
    candis = []
    for c in comb(N,M):
        if checkCandi(c):
            candis.extend(c)
            cnt += 1
    
    N = list(set(N).difference(set(candis)))
    M += 1

print(cnt)