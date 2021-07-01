def solution(n):
    answer = 0
    f1=0
    f2=1
    for i in range(2,n+1):
        answer = f1+f2
        f1 = f2
        f2 = answer
    return answer%1234567