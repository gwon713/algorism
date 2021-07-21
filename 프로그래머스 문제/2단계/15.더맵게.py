import heapq

def shake(scoville):
    return heapq.heappop(scoville)+heapq.heappop(scoville)*2

def solution(scoville, K):
    heapq.heapify(scoville)
    shakeCnt = 0
    while scoville[0] < K:
        try:
            heapq.heappush(scoville,shake(scoville))
        except IndexError:
            return -1
        shakeCnt+=1
        
    return shakeCnt