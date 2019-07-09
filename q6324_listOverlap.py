#Q6324. 리스트에서 중복된 항목 제거하기

exampleList = [1,2,3,4,3,2,1]

for i in range(0,len(exampleList)):
    for j in range(i+1, len(exampleList)):
        if exampleList[i] == exampleList[j]:
            del(exampleList[j]) # = 0
        print("i : {0}, j : {1}, list: {2}".format(i,j,exampleList))
    
print(exampleList)

# i : 0, j : 1, list: [1, 2, 3, 4, 3, 2, 1]
# i : 0, j : 2, list: [1, 2, 3, 4, 3, 2, 1]
# i : 0, j : 3, list: [1, 2, 3, 4, 3, 2, 1]
# i : 0, j : 4, list: [1, 2, 3, 4, 3, 2, 1]
# i : 0, j : 5, list: [1, 2, 3, 4, 3, 2, 1]
# i : 0, j : 6, list: [1, 2, 3, 4, 3, 2]
# i : 1, j : 2, list: [1, 2, 3, 4, 3, 2]
# i : 1, j : 3, list: [1, 2, 3, 4, 3, 2]
# i : 1, j : 4, list: [1, 2, 3, 4, 3, 2]
# i : 1, j : 5, list: [1, 2, 3, 4, 3]
# i : 2, j : 3, list: [1, 2, 3, 4, 3]
# i : 2, j : 4, list: [1, 2, 3, 4]
# [1, 2, 3, 4]