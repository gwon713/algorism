"""1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
가로의 숫자를 입력하시오 : 
세로의 숫자를 입력하시오 : """
width = int(input('가로의 숫자를 입력하시오 : '))
height = int(input('세로의 숫자를 입력하시오 : '))
a= '★'*width
for i in range(height):
	print(a)
	