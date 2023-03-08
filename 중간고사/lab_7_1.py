list = []
a = input('좋아하는 과일 이름을 입력하시오: ')
list.append(a)
b = input('좋아하는 과일 이름을 입력하시오: ')
list.append(b)
c = input('좋아하는 과일 이름을 입력하시오: ')
list.append(c)


fruit = input('과일 이름을 입력하세요: ')

if fruit in list:
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')   
