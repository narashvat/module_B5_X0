import random

def intial_message():
    print("          *************************")
    print("           Игра Крестики - Нолики")
    print("          *************************")
    print("")
    print("             Ваше игровое поле")
    print("              ----------------")
    print("              |  1 |  2 |  3 |")
    print("              ----------------")
    print("              |  4 |  5 |  6 |")
    print("              ----------------")
    print("              |  7 |  8 |  9 |")
    print("              ----------------")
    print("")
    print("Выбери цифру куда хочешь поставить Крестик!")


pole = [" "] * 9

def show():
    print("             Ваше игровое поле")
    print("              -------------")
    for i in range(0, 9, 3):
        print(f"              | {pole[i]} | {pole[i+1]} | {pole[i+2]} |")
        print("              -------------")
    print("")


def move():
    while True:
        numbers = input("Ваш ход: ").strip()

        if not numbers.isdigit():
            print("Введите число!")
            continue

        x = int(numbers) - 1

        if x < 0 or x > 8:
            print("Только числа от 1 до 9!")
            continue

        if pole[x] != " ":
            print("Клетка занята!")
            continue

        return x

def check_win():
    win_number = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for number in win_number:
        symbols = []
        for c in number:
            symbols.append(pole[c[0] * 3 + c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


intial_message()
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
        x = move()
        pole[x] = "X"
    else:
        print(" Ходит нолик!")
        available_moves = [i for i, value in enumerate(pole) if value == " "]
        x = random.choice(available_moves)
        pole[x] = "0"

    if check_win():
        show()
        break

    if count == 9:
        print(" Ничья!")
        break




