a = input()

ref = 'abcdefghijklmnopqrstuvwxyz'

for letter in ref:
    try:
        print(a.index(letter), end=' ')
    except:
        print(-1, end=' ')
        