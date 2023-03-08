x = int(input('첫 번째 숫자 입력:'))
y = int(input('두 번째 숫자 입력:'))

print(x * (y % 10))
print(x * ((y//10) % 10))
print(x * (y//100))
print(x * y)