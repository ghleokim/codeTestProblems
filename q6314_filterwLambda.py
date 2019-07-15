#Q6319. filter와 lambda로 조건문에 맞는 숫자 빼내기

a = list(range(1,11))
b = list(filter(lambda x: x % 2 == 0,a))
print(b)