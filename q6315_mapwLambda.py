#Q6315 map과 lambda로 제곱 값을 갖는 리스트 반환
a = list(range(1,11))
print(list(map(lambda x: x*x, a)))