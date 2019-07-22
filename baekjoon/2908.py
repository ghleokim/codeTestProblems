a = input().split()
if int(a[0][::-1]) > int(a[1][::-1]):
    print(a[0][::-1])
else:
    print(a[1][::-1])