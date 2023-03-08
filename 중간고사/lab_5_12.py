import random

while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(a, '+', b, '=', end = '') # end = '' 줄바꿈 없애는 것
    answer = int(input())

    if answer == a + b:
        print('잘했어요!!')
    else:
        print('정답은', a + b, '입니다. 다음번에는 잘할 수 있죠?')    
