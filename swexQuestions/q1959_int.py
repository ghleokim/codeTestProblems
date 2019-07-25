# ##

# [a1,a2,a3]
# [b1,b2,b3,b4,b5]

# range(l = len(a)-len(b))회 반복
# 0번째: a[0]   * b[0]
# 1번째: a[0+1] * b[0]
# ...

for k in range(int(input())):
    (n, m), a, b = map(lambda x: x.split(),(input(), input(), input()))
    (n,m),a,b = map(int,(n,m)), list(map(int,a)), list(map(int,b))
	
    if n<m:
        a,b =b,a
    l =abs(n-m)+1
    res = [0] * l
    for i in range(l):
        for j in range(len(b)):
            res[i] += a[j+i] * b[j]
    print(f'{k} {max(res)}')

###

# a = [3,6,-7,5,4]
# b = [1,5,3]

# print(sum(map(lambda x:x[0]*x[1],(zip(a[2:],b)))))

###숏

for k in range(int(input())):
    (n,m),a,b=map(lambda x: x.split(),(input(),input(),input()))
    (n,m),a,b=map(int,(n,m)),list(map(int,a)),list(map(int,b))
    if n<m:a,b=b,a
    l,r=abs(n-m)+1,[0]*l
    for i in range(l):
        r[i]=sum(map(lambda x:x[0]*x[1],(zip(a[i:],b))))
    print(f'#{k+1} {max(r)}')

###숏숏
for k in range(int(input())):
    (n,m),a,b=map(lambda x: x.split(),(input(),input(),input()))
    a,b=list(map(int,a)),list(map(int,b))
    l=len(a)-len(b)
    if l<0:a,b=b,a
    r=[]
    for i in range(abs(l)+1):
        r.append(sum(map(lambda x:x[0]*x[1],(zip(a[i:],b)))))
    print(f'#{k+1} {max(r)}')