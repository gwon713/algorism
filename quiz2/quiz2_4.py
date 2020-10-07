'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오
테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()
<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''   
class YCard:
    def consumeY(self,spend):
        self.spend = spend - (spend * 0.2)
class MCard:
    def consumeM(self,spend):
        self.spend = spend - (spend * 0.1)
class GCard:
    def consumeG(self,spend):
        self.spend = spend - (spend * 0.1)
class Multi_card(YCard,MCard,GCard):
    money = 0
    def __init__(self):
        print('카드가 발급 되었습니다.')
    
    def charge(self,num):
        self.money = self.money + num
        print('잔액이 {}원 입니다.'.format(self.money))
    def consume(self,spend,place):
        if place == '영화관':
            self.consumeY(spend)
        elif place == '마트':
            self.consumeM(spend)
        else :
            self.consumeG(spend)
        if self.money >= self.spend :
            self.money = self.money - self.spend
            print("{}에서 {}원 사용했습니다.".format(place,int(self.spend)))
        else : 
            print("잔액이 부족합니다.")
    def print(self):
        print("잔액이 {}원 입니다.".format(int(self.money)))
        
        
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()