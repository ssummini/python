import random

list = []
for i in range(3):
    list.append(random.randint(0,9))
print(list)

a, b, c = map(int, input('세 복권번호를 입력하세요 : ').split())

for i in range(len(list)):
    count = 0
    if a in list:
        count += 1
    if b in list:
        count += 1
    if c in list:
        count += 1


if count == 3:
    print('1억원')
if count == 2:
    print('1천만원')
if count == 1:
    print('1만원')
if count == 0:
    print('다음기회에..')