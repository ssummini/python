def max(n1, n2, n3):
    list = [n1, n2, n3]
    list.sort()
    return list[2]

def min(n1, n2, n3):
    list = [n1, n2, n3]
    list.sort()
    return list[0]

n1, n2, n3 = map(int, input('세 정수를 입력하시오:').split())
print('가장 큰 수 : ', max(n1, n2, n3))    
print('가장 작은 수 : ', min(n1, n2, n3))    