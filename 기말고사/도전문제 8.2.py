# 8장 연관된 데이터를 딕셔너리로 짝을 짓자

phone_book = {}  # 공백 딕셔너리를 생성
phone_book["홍길동"] = "010-1234-5678"
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"


# print(phone_book.keys())
# print(phone_book.values())

# for name, phone_num in phone_book.items():
#     print(name, ":", phone_num)

# for key in phone_book.keys():
#     print(key, ':', phone_book[key])

# print(sorted(phone_book))
# sorted_phone_book = sorted(phone_book.items(), key=lambda x: x[0])
# print(sorted_phone_book)

# del phone_book["홍길동"]
# print(phone_book)

# t = (100, 200, 300)
# print((lambda x: x[0])(t))


# 람다함수
# sorted_phone_book1 = sorted(phone_book.items(), key=lambda x: x[0]) #이름으로 정렬
# sorted_phone_book2 = sorted(phone_book.items(), key=lambda x: x[1]) #번호로 정렬
# print(sorted_phone_book1)
# print(sorted_phone_book2)

stock_dict = {}
stock_dict["콜라"] = 4

while True:

    menu = int(input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료:"))

    if menu == 1:
        name = input("[재고조회] 물건의 이름을 입력하시오:")
        print("재고 : ", stock_dict[name])

    elif menu == 2:
        name, num = (input("[입고] 물건의 이름과 수량을 입력하세요: ")).split()
        num = int(num)
        if name in stock_dict.keys():
            stock_dict[name] += num

        else:
            stock_dict[name] = num
        print("재고:", stock_dict[name])

    elif menu == 3:
        name, num = (input("[출고] 물건의 이름과 수량을 입력하세요:")).split()
        num = int(num)
        if name in stock_dict.keys():
            stock_dict[name] -= num
        else:
            stock_dict[name] = num
        print("재고:", stock_dict[name])

    elif menu == 4:
        print("프로그램을 종료합니다.")
        break



    