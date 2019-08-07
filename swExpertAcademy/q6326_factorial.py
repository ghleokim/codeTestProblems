#Q6326 팩토리얼

def factorial(number):
    result = 1
    for i in range(number,0,-1):
        result *= i
    return result

num = int(input())

print(factorial(num))