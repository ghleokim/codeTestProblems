def tri(n,i=0,res=[]):
    if i==0:
        res=[]
    quotient, remainder = (n-1) // 3, (n-1) % 3
    if remainder == 0:
        res.append('1')
    elif remainder == 1:
        res.append('2')
    else:
        res.append('4')
    if not quotient:
        return ''.join(res[::-1])
    else:
        return tri(quotient, i+1, res)

for i in range(1,15):
    print(i, tri(i))

##
def change124(n):
    num='124'
    answer=''

    while(n>0):
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    
    return answer

print(change124(10))