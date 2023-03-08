import random
list = []
value = -1
while value <= 0:
    value = random. randint(-5, 5)
    list.append(value)
    
print(list)

# def order(burger_num, patty = 1 , cheese = 1 , double_burger = False):
#     if double_burger == True:
#         print('햄버거 {}개 주문, 패티 {}, 치즈 {}'.format(burger_num, patty*2, cheese*2))
#     else:
#         print('햄버거 {}개 주문, 패티 {}, 치즈 {}'.format(burger_num, patty, cheese))


# order(1, 2, 2, True)
# order(2)

# list = 'hello'
# print([x.upper() for x in list])
# arr = [0 for i in range(8)]
# print(arr)