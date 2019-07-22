#Q6321. 소수를 검사하는 함수

number = int(input())

def checkPrime(num):
    result = True
    for i in range(2,num):
        if num % i == 0:
            result = False
    if result:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")
    return

checkPrime(number)