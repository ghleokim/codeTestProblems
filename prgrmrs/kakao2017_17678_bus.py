def solution(n, t, m, timetable): # 17678
    answer = ''
    
    # timetext: 시간 배열을 분으로 표시
    timetext = []
    for tt in timetable:
        timetext.append(int(tt[:2])*60+int(tt[-2:]))
    
    timetext.sort()
    
    passengerid = [None for _ in range(n)]
    bustime = 540
    person = 0
    for bus in range(n):
        bustime = 540 + bus * t
        jungwon = m
        for i in range(m):
            if person == len(timetable):
                break
            elif timetext[person] <= bustime and jungwon > 0:
                if passengerid[bus]:
                    passengerid[bus].append(person)
                else:
                    passengerid[bus] = [person]
                person += 1
                jungwon -= 1
            else:
                break
    
    # 마지막 버스에 승객 탑승이고 만석일 때: 마지막 승객 - 1분
    if passengerid[-1] and len(passengerid[-1]) == m:
        offset = timetext[passengerid[-1][-1]]-541
        answer = f'{9+offset//60:0>2}:{offset%60:0>2}'
    else:
        offset = (n-1)*t
        answer = f'{9+offset//60:0>2}:{offset%60:0>2}'
    
    
    return answer

