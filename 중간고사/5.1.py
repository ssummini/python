print('1에서 100까지의 수 중에서 홀수는 : ')
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end = ' ')


print('1에서 100까지의 수 중에서 홀수는 : ')
i = 1
while i < 101:
    if i % 2 == 1:
        print(i, end = ' ')
    i += 1