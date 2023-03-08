total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total = total + i
print('1에서 100까지의 수 중에서 홀수의 합 : ', total)        



'''
start = int(input('시작 정수를 입력하세요 : '))
end = int(input('끝 정수를 입력하세요 : '))

total = 0
for i in range(start, end+1):
    total = total + i
print(start, '에서', end, '까지 정수의 합 : ', total)  
'''  