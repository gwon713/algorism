"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""
width = float(input('삼각형의 가로를 입력하세요 : '))
height = float(input('삼각형의 높이를 입력하세요 : '))

print('삼각형의 넓이 : {}'.format(round(width*height/2, 3)))