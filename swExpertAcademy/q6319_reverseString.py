#Q6319. 반복문을 이용해 단어를 거꾸로 하는 함수

string = input()

def flip_string(target):
    flipped_string = target[len(target)-1]
    for i in range(len(target)-2,-1,-1):
        flipped_string += target[i] 
    return flipped_string

print(flip_string(string))
print(flip_string==string)

if flip_string==string:
    print("입력하신 단어는 회문(Palindrome)입니다.")

# string = input()

# def flip_string(target):
#     return target[::-1]

# print(flip_string(string))

# if flip_string(string)==string:
#     print("입력하신 단어는 회문(Palindrome)입니다.")