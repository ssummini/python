import random

def basic(min, max, length):
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

if __name__ == "__main__":
    min, max, length = map(int, input('세 숫자를 입력하세요:').split())
    print(basic(min, max, length))

