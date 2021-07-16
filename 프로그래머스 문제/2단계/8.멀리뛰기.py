def solution(n):
    if n < 3: return n
    n1, n2 = 1, 2
    for i in range(3,n+2):
        n1, n2 = n2, n1 + n2
    return n1%1234567