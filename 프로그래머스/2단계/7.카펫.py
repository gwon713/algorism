def solution(brown, yellow):
    answer = [0,0]
    total = brown+yellow
    for i in range(1,total):
        if total%i==0:
            a=i
            b=total/i
            if (a-2)*(b-2)==yellow:
                answer[0]=max(a,b)
                answer[1]=min(a,b)
    return answer