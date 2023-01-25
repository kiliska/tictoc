print("<" * 3, " Игра Крестики-нолики", ">" * 3)
field = list(range(1,10))

def draw(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-" * 13)

def ask():
    while True:
        cell = input('Номер ячейки для хода - ')

        x = cell

        if not(x.isdigit()):
            print('Введите число!')
            continue

        x = int(x)

        if x == 0 or x > 10:
            print('Ваш выбор вне диапазона от 1 до 9!')
            continue
        x -= 1
        if field[x] == "X" or field[x] == "O":
            print("Клетка занята!")
            continue
        return x

def victory():
    win_ = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]
    for x in win_:
        if field[x[0]] == field[x[1]] == field[x[2]]:
            return field[x[0]]
    return False

num = 0
while True:
    num += 1

    draw(field)

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print('Ходит нолик')
    x = ask()
    if num % 2 == 1:
        field[x] = "X"
    else:
        field[x] = "O"
    if victory():
        draw(field)
        print('Крестик победил!' if num % 2 == 1 else 'Нолик победил!')
        break
    if num == 9:
        draw(field)
        print('Ничья')
        break




