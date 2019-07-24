# for i in range(int(input())):
#     (n, m), a, b = map(lambda x: x.split(),(input(), input(), input()))
    
#     len(a)
#     len(b)
#     res = 0
#     #a가 더 작다고 가정.
#     for j in range(len(b)-len(a)):
#         for k in range(len(a)):
#             res += a[k]*b[j+k]
        
#     print(res)

# ##

# [a1,a2,a3]
# [b1,b2,b3,b4,b5]

# range(l = len(a)-len(b))회 반복
# 0번째: a[0]   * b[0]
# 1번째: a[0+1] * b[0]
# ...

#a가 더 길 때

# a = [3,6,-7,5,4]
# b = [1,5,3]

# l = len(a) - len(b)
# print(l)
# res = [0] * (l+1)

# for i in range(l+1):
#     for j in range(len(b)):
#         print(f'i:{i},j:{j}')
#         res[i] += a[j+i] * b[j]
#     print(res[i])

# print(res)

###

a = [3,6,-7,5,4]
b = [1,5,3]

print(sum(map(lambda x:x[0]*x[1],(zip(a[2:],b)))))


# for k in range(int(input())):
#     (n, m), a, b = map(lambda x: x.split(),(input(), input(), input()))
#     (n,m),a,b = map(int,(n,m)), list(map(int,a)), list(map(int,b))
	
#     if n<m:
#         a,b =b,a
#     l =abs(n-m)+1
#     res = [0] * l
#     for i in range(l):
#         for j in range(len(b)):
#             res[i] += a[j+i] * b[j]
#     print(f'{k} {max(res)}')

###

# for k in range(int(input())):
#     (n,m),a,b=map(lambda x: x.split(),(input(),input(),input()))
#     (n,m),a,b=map(int,(n,m)),list(map(int,a)),list(map(int,b))
#     if n<m:
#         a,b=b,a
#     l=abs(n-m)+1
#     r=[0]*l
#     for i in range(l):
        
#         # for j in range(len(b)):
#         #     r[i]+=a[j+i]*b[j]
#     print(f'#{k+1} {max(r)}')