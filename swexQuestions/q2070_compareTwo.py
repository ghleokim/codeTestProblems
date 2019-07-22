#q2070 
num = int(input())

def comparison(a, b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '='

for enum in range(1,num+1):
    c = input().split(' ')
    if c[-1] == '':
        c.pop(-1)

    a, b = int(c[0]), int(c[1])
    
    print('#{0} {1}'.format(enum, comparison(a,b)))