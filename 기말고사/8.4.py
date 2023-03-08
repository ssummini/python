print('100과 200의 합 :', (lambda x, y: x + y)(100, 200))

t = (100, 200, 300)
print((lambda x:x[0])(t))
print((lambda x:x[1])(t))

phone_book = {'홍길동' : '010-1234-5678'}
phone_book['강감찬'] = '010-1234-5679'
phone_book['이순신'] = '010-1234-5670'

print(phone_book.items())

print('-----------------------------------')
sorted_phone_book1 = sorted(phone_book.items(), key=lambda x:x[0])
print(sorted_phone_book1)

print('-----------------------------------')
sorted_phone_book2 = sorted(phone_book.items(), key=lambda x:x[1])
print(sorted_phone_book2)
