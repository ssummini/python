price = int(input('물건 가격:'))
charge = 1000 - price

a = charge // 500
b = (charge % 500) // 100
c = ((charge % 500) % 100) // 50
d = (((charge % 500) % 100) % 50) // 10

print(a + b + c + d)