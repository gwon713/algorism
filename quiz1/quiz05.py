"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
num = int(input('몇단을 출력하시겠습니까? : '))

if 0 <= num and 9 < num :
    print('error')
else :
    print('------- {}단 -------'.format(num))
    for i in range(1,10) : 
        print('{} * {} = {}'.format(num,i,num*i))
    