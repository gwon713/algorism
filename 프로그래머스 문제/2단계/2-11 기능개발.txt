def solution(progresses, speeds):
    answer = []
    day = [0]*len(progresses)
    for i in range(0,len(progresses)):
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            day[i]+=1
    cnt=1
    for i in range(1,len(day)):
        if day[i-1]>day[i]:
            day[i]=day[i-1]
    for i in range(1,len(day)):
        if day[i-1]>=day[i]:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    return answer