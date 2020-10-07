"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
dice = [1,2,3,4,5,6]


input('player1 : Enter key를 눌러 주사위를 던져주세요')
import random
p1 = random.choice(dice)
print('player1 : {}'.format(p1))

input('player2 : Enter key를 눌러 주사위를 던져주세요')
import random
p2 = random.choice(dice)
print('player2 : {}'.format(p2))

print('--------------')
if p1 > p2 :
    print('player1 Win')
elif p2 > p1 :
    print('player2 Win')
else :
    print('Draw')