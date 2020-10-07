"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""

num = int(input('점수를 입력해주세요 : '))

if 80 < num < 101 : 
    print('A')
elif 60 < num < 81 :
    print('B')
elif 40 < num < 61 :
    print('C')
elif 20 < num < 41 :
    print('D')
elif 0 <= num < 101 :
    print('F')
else :
    print('error')