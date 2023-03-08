from 기본 import basic

def find_zero(result, min, max, length):
    print(result)
    while True:
        if 0 in result:
            return result
        else:
            result = basic(min, max, length)
            print(result)
                
if __name__ == "__main__":
    min, max, length = map(int, input('세 숫자를 입력하세요:').split())
    result = basic(min, max, length)
    find_zero(result, min, max, length)

    
