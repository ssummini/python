from tkinter.messagebox import YES


total = 0
answer = 'yes'

while answer == 'yes':
    num = int(input('숫자를 입력하시오: '))
    total = total + num
    answer = input('계속?(yes/no): ')

print('합계는 : ', total)