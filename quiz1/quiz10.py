"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

num = int(input('정수를 입력해주세요 : '))
def factoral(num) : 
    for i in range(1,num) :
        num = num * i
    return num
print(factoral(num))