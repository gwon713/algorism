"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """

num = input('주민등록번호를 입력해주세요(13자리): ')


main_num = num.split("-")
 

sub_num = main_num[1]
s_num = sub_num[0:1]

if s_num == '1' or s_num == '3' :
    print('남자입니다.')
elif s_num == '2' or s_num == '4' :
    print('여자입니다.')
else :
    print('error')

