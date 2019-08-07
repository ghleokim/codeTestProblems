#Q6320. 가위바위보

def checkWinner(p1, p2):
    def printWinner(p):
        print("{0}가 이겼습니다!".format(p))
        return

    if p1 == p2:
        print("비겼습니다!")
    elif p1 == "가위":
        if p2 == "보":
            return printWinner(p1)
        else:
            return printWinner(p2)
    elif p1 == "바위":
        if p2 == "가위":
            return printWinner(p1)
        else:
            return printWinner(p2)
    else:
        if p2 == "바위":
            return printWinner(p1)
        else:
            return printWinner(p2)

key1 = input()
key2 = input()
dat1 = input()
dat2 = input()

data = {}

data[key1] = dat1
data[key2] = dat2

checkWinner(data[key1], data[key2])