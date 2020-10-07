"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""

change_word = input('영어를 입력해주세요 : ')

if 'a'<=change_word<='z' : 
    print(change_word.upper())
elif 'A'<=change_word<='Z' :
    print(change_word.lower())
else :
    print('입력 형식이 잘못되었습니다')