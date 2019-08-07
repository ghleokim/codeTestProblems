c = int(input())
n = int(input())
li = [1,0,0,0,0,0,0,0,0,0]
print(li)
newli = li


newli[0] = li[0]
for col in range(1,10):
    newli[col] = li[col-1]+li[col]
print(newli)