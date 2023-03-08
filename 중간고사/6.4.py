def max_and_min(arr):
    arr.sort()
    print("가장 큰 수 : ", arr[2])
    print("가장 작은 수 : ", arr[0])


if __name__ == "__main__":
    list1 = list(input("3 수를 입력하시오: ").split())
    max_and_min(list1)