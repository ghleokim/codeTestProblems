#Q6327 제곱 값 출력

def square(num):
    return num * num

tar = input()
tar = tar.split(', ')

for number in tar:
    print("square({0}) => {1}".format(int(number), int(number) * int(number)))