def hanoi(disk, tower1, tower2, tower3):
    if disk==0: return
    hanoi(disk-1,tower1,tower3,tower2)
    print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(tower1,disk,tower3))
    hanoi(disk-1,tower2,tower1,tower3)

hanoi(3,1,2,3)
