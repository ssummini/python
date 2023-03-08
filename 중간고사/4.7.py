import random

a = random.randint(1, 100)
b = random.randint(1, 100)

print(a, b)

sum = int(input('a + b = '))

if sum == a + b:
    print('잘했어요!!')
else:
    print('정답은', a+b, '입니다.')   