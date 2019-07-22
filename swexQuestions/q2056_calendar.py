#q2056
num = int(input())

dayChart = {
    31: [1,3,5,7,8,10,12],
    30: [4,6,9,11],
    28: [2]
}

def checkDate(year, month, day):
    if int(month) > 12 or int(month) < 1 or int(day) < 1:
        return -1
    else:
        for d, m in dayChart.items():
            if (int(month) in m) and (int(day) <= d):
                return '{0}/{1}/{2}'.format(year, month, day)
        return -1

for case in range(num):
    inDate = input()

    year = inDate[:4]
    month = inDate[4:6]
    day = inDate[6:]
    
    print('#{0} {1}'.format(case+1, checkDate(year, month, day)))