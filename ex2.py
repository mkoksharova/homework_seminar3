import random


def generate_list(quantity):
    list = []
    for i in range(quantity):
        list.append(random.randint(0, 10))
    return list


def multiply_pairs(list):
    pairs = []
    for i in range(len(list) // 2):
        pairs.append(list[i] * list[len(list) - i - 1])
    if len(list) % 2 != 0:
        pairs.append(list[len(list) // 2]**2)
    return pairs


def main():
    quantity = int(input("Введите количество элементов списка: "))
    list = generate_list(quantity)
    print("Список:", list)
    print("Произведение пар чисел списка:", multiply_pairs(list))


main()