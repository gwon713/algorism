def solution(people, limit) :
    answer = 0
    people.sort()

    li = 0
    hv = len(people) - 1
    while li < hv :
        if people[li] + people[hv] <= limit :
            li += 1
            answer += 1
        hv -= 1
    return len(people) - answer