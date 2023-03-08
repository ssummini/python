def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True

n = int(input('소수 검사를 할 정수를 입력하시오: '))
print('소수인가요? : ', is_prime(n))            