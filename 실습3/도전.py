a, b = map(int, input('두 정수를 입력하시오:').split())

c = a ^ b
d = c // 16
e = c % 16
pw = d * e

print(str(pw) * 2)