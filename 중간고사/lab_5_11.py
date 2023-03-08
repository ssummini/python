import random

tries = 0
guess = 0
num = random.randint(1, 100)
print(num)

while guess != num:
    guess = int(input('숫자를 입력하시오: '))
    tries += 1

    if guess < num:
        print('낮음!')
    elif guess > num:
        print('높음!')

print('축하합니다. 총 시도횟수 = ', tries)