# 개미군단 : https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    answer = 0
    if hp // 5 > 0 :
        answer += hp // 5
        hp = hp % 5
    if hp // 3 > 0 :
        answer += hp // 3
        hp = hp % 3
    if hp // 1 > 0  :
        answer += hp // 1
    return answer