"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""

for i in range(1,101):
    result = i
    
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        result = '짝'
    elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        result = '짝'
    elif i % 5 == 0:
        result = '아자'
    print(result)
    
    
