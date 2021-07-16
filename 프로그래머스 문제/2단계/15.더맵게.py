def shake(scoville):
    return scoville.pop(0)+(scoville.pop(0)*2)

def solution(scoville, K):
    shakeCnt = 0
    while min(scoville) < K:
        if len(scoville)>1:
            scoville.sort()
            scoville.append(shake(scoville))
            shakeCnt+=1
        else:
            return -1
        
    return shakeCnt


def shake(scoville):
    return scoville.pop(0)+(scoville.pop(0)*2)

def solution(scoville, K):
    shakeCnt = 0
    while min(scoville) < K:
        scoville.sort()
        try:
            scoville.append(shake(scoville))
        except IndexError:
            return -1
        shakeCnt+=1
        
    return shakeCnt