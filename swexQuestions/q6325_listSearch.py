#Q6325 리스트에서 특정 숫자 검색, 임의의 숫자 포함 여부 출력

def search(element, targetList):
    for i in targetList:
        if i == element:
            return True
    return False

smList = [2,4,6,8,10]
print(smList)

searchTar = [5, 10]

for tar in searchTar:
    print("{0} => {1}".format(tar,search(tar,smList)))
