phone_book = {'홍길동' : '010-1234-5678'}
phone_book['강감찬'] = '010-1234-5689'
phone_book['이순신'] = '010-1234-5680'

print(phone_book)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

for phone_num, name in phone_book.items():
    print(phone_num, ':', name)

print('-----------------------------------')
for key in phone_book.keys():
    print(key, ':', phone_book[key])  

print('-----------------------------------')
print(sorted(phone_book)) # 키 기준으로 정렬      

print('-----------------------------------')
sorted_phone_book = sorted(phone_book.items(), key=lambda x:x[0])
print(sorted_phone_book)

print('-----------------------------------')
del phone_book["홍길동"]
print(phone_book)