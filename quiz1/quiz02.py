""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""
num1 = float(input('첫번째 수 입력 : '))
num2 = float(input('두번째 수 입력 : '))
cal= input('연산기호 입력 : ')


if cal == '+':
    result = num1 + num2
    print(result)
elif cal == '-' and num1 >= num2:
    result = num1 - num2
    print(result)
elif cal == '*':
    result = num1 * num2
    print(result)
elif cal == '/':
    result = num1 / num2
    print(result)
elif cal == '%':
    result = num1 % num2
    print(result)
else:
    print('error')