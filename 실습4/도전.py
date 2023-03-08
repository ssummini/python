
from 기본 import basic
from 심화 import find_zero

def plus(list) :
    array = []
    for i in range(len(list)-1):
        first = list[i]
        second = list[i+1]
        array.append(list[i])
        array.append((first+second)/2)
    array.append(list[len(list)-1]) #마지막 원소 넣어주기
    print(array)


if __name__ == "__main__" :
    min, max, length = map(int, input("세 숫자를 입력하시오: ").split())
    array1 = basic(min, max, length)
    array2 = find_zero(array1, min, max, length)
    plus(array2)
    
