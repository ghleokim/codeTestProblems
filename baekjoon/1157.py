a = input().upper()
ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = []
for letter in ref:
    counter.append(a.count(letter))
if counter.count(max(counter)) > 1:
    print('?')
else:
    print(ref[counter.index(max(counter))])

