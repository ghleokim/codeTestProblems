num = int(input())

for enum in range(1,num+1):
    c = input()
    d = c.split(' ')
    print(r'#{0} {1}'.format(enum, sum(map(lambda x: x if x % 2 else 0, c.split(' ')))))