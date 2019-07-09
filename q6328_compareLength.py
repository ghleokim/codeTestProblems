#Q6328 문자열 길이 비교하기

inp = input()
inList = inp.split(', ')

for i in range(1,len(inList)):
    # 1번째-2번째 비교
    # 1번째가 더 크면 1번째 3번째 비교
    # 2번째가 더 크면 2번째 3번째 비교
    # 앞선 것들 중 가장 큰 것과 n번째 비교
    if i == 1:
        j = 0

    if inList[j] > inList[i]:
        j = j
    elif inList[j] < inList[i]:
        j = i
    else:
        print("Same")

print(inList[j])



    
