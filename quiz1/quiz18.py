"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']
"""

file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
main_file = [0 for i in range(len(file))]
for i in range(len(file)) : 
    main_file[i] = file[i].split('.')[0]

print(main_file)
