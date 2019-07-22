#Q6329. 카운트다운하는 함수 정의.

a = [0, 10]

def countdown(number):
    if number <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(number,0,-1):
            print(i)
    

for elem in a:
    countdown(elem)