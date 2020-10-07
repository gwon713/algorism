"""11. 최대공약수를 구하는 함수를 구현하시오"""

num1 = int(input('정수1을 입력해주세요 : '))
num2 = int(input('정수2을 입력해주세요 : '))

num1_list = []
num2_list = []

for i in range(1,num1+1):
    if num1 % i == 0:
        num1_list.append(i)
 
for i in range(1,num2+1):
    if num2 % i == 0:
        num2_list.append(i)

print(num1_list,num2_list)

num_list = []

for i in range(len(num1_list)):
    for j in range(len(num2_list)):
        if num1_list[i] == num2_list[j]:
            num_list.append(num1_list[i])

print('두 수의 최대공약수는 : {}'.format(num_list[-1]))