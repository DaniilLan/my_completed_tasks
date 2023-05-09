def sort_list(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)
    return arr


def binary_search(arr, x):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            first = mid + 1
        else:
            last = mid - 1
    return first



input_str = input("Введите последовательность чисел через пробел: ")
try:
    input_list = [int(x) for x in input_str.split()]
except ValueError:
    print("Вы ввели некорректные данные")
else:
    num = input("Введите число: ")
    try:
        num = int(num)
    except ValueError:
        print("Вы ввели некорректное число")
    else:
        sort_list = sort_list(input_list)
        position = binary_search(sort_list, num)
        if position == len(sort_list):
            print("Введенное число больше всех элементов в последовательности")
        elif position == 0 and sort_list[position] != num:
            print("Введенное число меньше всех элементов в последовательности")
        else:
            print(f"Позиция элемента: {position} (не индекс)")
