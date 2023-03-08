print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
s = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
a, b = map(int, input('연산을 원하는 숫자 두개를 입력하세요 \n').split())

if s == 1:
    print(a, '+', b, '=', a+b)
elif s == 2:
    print(a, '-', b, '=', a-b)
elif s == 3:
    print(a, '*', b, '=', a*b)
elif s == 4:
    print(a, '/', b, '=', a/b)    