#Q6323 피보나치 수열

number = int(input())

def fibonacciNumbers(num):
    result = []
    result.append(1)
    result.append(1)

    for i in range(2,num):
        result.append(result[i-1] + result[i-2])
    return result

print(fibonacciNumbers(number))