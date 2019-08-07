# c = int(input())
# for i in range(1,c+1):
#     li = list(map(int,input().split()))
#     a = li[0] * li[4]
#     b = li[1]
#     if li[4] > li[2]:
#         b += (li[4]-li[2]) * li[3]
#     print(f'#{i} {min(a,b)}')

# c=int(input())
# for i in range(c):
#     l=list(map(int,input().split()))
#     print(f'#{i+1} {min(l[0]*l[4],l[1] if l[4]<l[2] else l[1]+(l[4]-l[2])*l[3])}')
#
c=int(input())
for i in range(c):
    p,q,r,s,w=map(int,input().split())
    print(f'#{i+1} {min(p*w,q if w<r else q+(w-r)*s)}')
#q+(w-r)*s
#w*s-q*(s-1)
#

#   0,1,2,3,4
#   p,q,r,s,w
#   a : p * w
#   b : w<r --- q
#       w>r --- q + (w-q) * s = w * s - q * (s-1)