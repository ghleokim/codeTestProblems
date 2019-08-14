# 나무재테크

# (n-1)*(n-1)의 크기를 가진 리스트:
#
# nutrition = []
# s2d2 = []
# died = []
# age = []

# 크기가 변할 수 있는 자료:
#
#
# n = 5 
# trees = [[]] * (n-1) * (n-1)

# # if tree[0] == []:
# #     print('a')

# a = [None]

# # 죽는 나무 나이 계산하기
# print(sum(map(lambda x : x // 2, a[1:])))



def getRC(r,c):
    return r * n + c

n = 10

nutrition = [5] * n * n
trees = [0] * n * n
died = [0] * n * n

print(trees)
print(nutrition)

def spring(): #


    # for en, tree in enumerate(trees):
    #     if tree:            # calculate nutrition
    #         print(en,nutrition[en],tree)
    #         died[en] += sum(map(lambda x : x // 2, tree[1:]))  # calculate dying trees
    #         if tree[0] <= nutrition[en]:
    #             tree[0] += 1
    #             nutrition[en] -= tree[0]
    #             continue
    #         else:
    #             died[en] += tree[0]//2
    #             tree[0] = 0

spring()
print(nutrition)
print(died)


#     pass

# # ===============
# def summer():
#     return list(map(sum,zip(nutrition,died)))
#     pass

# def fall():
#     pass

# # ===============
# def winter():
#     return list(map(sum, zip(nutrition,s2d2)))
# nutrition = winter()
# # ===============


