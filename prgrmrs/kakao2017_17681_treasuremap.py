# https://programmers.co.kr/learn/courses/30/lessons/17681
# 방법 1: ''.join(string)
def solution1(n, arr1, arr2):
    answer = []
    tmp = [[' ' for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (arr1[i] & (1 << j)) or (arr2[i] & (1 << j)):
                tmp[i][n-j-1] = '#'

    for row in tmp:
        answer.append(''.join(row))

    return answer

# 방법2: string concatenation( 빠름 )
def solution2(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (arr1[i] & (1 << j)) or (arr2[i] & (1 << j)):
                answer[i] = '#' + answer[i]
            else:
                answer[i] = ' ' + answer[i]
                
    return answer

"""
방법 1: ''.join(string)
테스트 1 〉	통과 (0.11ms, 10.9MB)
테스트 2 〉	통과 (0.25ms, 10.8MB)
테스트 3 〉	통과 (0.06ms, 10.8MB)
테스트 4 〉	통과 (0.13ms, 10.8MB)
테스트 5 〉	통과 (0.09ms, 10.7MB)
테스트 6 〉	통과 (0.15ms, 10.8MB)
테스트 7 〉	통과 (0.08ms, 10.9MB)
테스트 8 〉	통과 (0.07ms, 10.8MB)
"""
"""
방법 2: string concatenation
테스트 1 〉	통과 (0.06ms, 10.7MB)
테스트 2 〉	통과 (0.09ms, 10.6MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.06ms, 10.7MB)
테스트 5 〉	통과 (0.05ms, 10.7MB)
테스트 6 〉	통과 (0.07ms, 10.7MB)
테스트 7 〉	통과 (0.05ms, 10.8MB)
테스트 8 〉	통과 (0.05ms, 10.7MB)
"""