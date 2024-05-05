igrok2 = ""

# 1. Выбор элемента
print("Игрок 1, выберите, чем будете играть. Введите 'x', если крестиком и 'o', если ноликом:")
igrok1 = input()

# 2. Поиск ошибки в вводе
while igrok1 != 'x' and igrok1 != 'o':
    print("Кажется, вы ввели не то значение, попробуйте снова:")
    igrok1 = input()

# 3. Выдача элемента второму игроку
if igrok1 == 'x':
    igrok2 = 'o'
elif igrok1 == 'o':
    igrok2 = 'x'

# 4. Построение поля
pole = [" ", 0, 1, 2,
        0, " ", " ", " ",
        1, " ", " ", " ",
        2, " ", " ", " "]


def vivod_polya():
    print(pole[0], end=" ")
    print(pole[1], end=" ")
    print(pole[2], end=" ")
    print(pole[3])

    print(pole[4], end=" ")
    print(pole[5], end=" ")
    print(pole[6], end=" ")
    print(pole[7])

    print(pole[8], end=" ")
    print(pole[9], end=" ")
    print(pole[10], end=" ")
    print(pole[11])

    print(pole[12], end=" ")
    print(pole[13], end=" ")
    print(pole[14], end=" ")
    print(pole[15])


vivod_polya()

# 5. Ход для первого игрока
print()
print("Вводите координаты, куда вы хотите поставить ваш символ, например: '00' (первое число - по горизонтали, второе - по вертикали)")


def hod1():
    hodd1 = input()
    while hodd1 != "00" and hodd1 != "01" and hodd1 != "02" and hodd1 != "10" and hodd1 != "11" and hodd1 != "12" and hodd1 != "20" and hodd1 != "21" and hodd1 != "22":
        print("Кажется, вы ввели не то значение, попробуйте снова:")
        hodd1 = input()

    if hodd1 == "00" and pole[5] == " ":
        pole.pop(5)
        pole.insert(5, igrok1)
        vivod_polya()
    if hodd1 == "01" and pole[6] == " ":
        pole.pop(6)
        pole.insert(6, igrok1)
        vivod_polya()
    if hodd1 == "02" and pole[7] == " ":
        pole.pop(7)
        pole.insert(7, igrok1)
        vivod_polya()
    if hodd1 == "10" and pole[9] == " ":
        pole.pop(9)
        pole.insert(9, igrok1)
        vivod_polya()
    if hodd1 == "11" and pole[10] == " ":
        pole.pop(10)
        pole.insert(10, igrok1)
        vivod_polya()
    if hodd1 == "12" and pole[11] == " ":
        pole.pop(11)
        pole.insert(11, igrok1)
        vivod_polya()
    if hodd1 == "20" and pole[13] == " ":
        pole.pop(13)
        pole.insert(13, igrok1)
        vivod_polya()
    if hodd1 == "21" and pole[14] == " ":
        pole.pop(14)
        pole.insert(14, igrok1)
        vivod_polya()
    if hodd1 == "22" and pole[15] == " ":
        pole.pop(15)
        pole.insert(15, igrok1)
        vivod_polya()


# 6. Ход для второго игрока
def hod2():
    hodd2 = input()
    while hodd2 != "00" and hodd2 != "01" and hodd2 != "02" and hodd2 != "10" and hodd2 != "11" and hodd2 != "12" and hodd2 != "20" and hodd2 != "21" and hodd2 != "22":
        print("Кажется, вы ввели не то значение, попробуйте снова:")
        hodd2 = input()

    if hodd2 == "00" and pole[5] == " ":
        pole.pop(5)
        pole.insert(5, igrok2)
        vivod_polya()
    if hodd2 == "01" and pole[6] == " ":
        pole.pop(6)
        pole.insert(6, igrok2)
        vivod_polya()
    if hodd2 == "02" and pole[7] == " ":
        pole.pop(7)
        pole.insert(7, igrok2)
        vivod_polya()
    if hodd2 == "10" and pole[9] == " ":
        pole.pop(9)
        pole.insert(9, igrok2)
        vivod_polya()
    if hodd2 == "11" and pole[10] == " ":
        pole.pop(10)
        pole.insert(10, igrok2)
        vivod_polya()
    if hodd2 == "12" and pole[11] == " ":
        pole.pop(11)
        pole.insert(11, igrok2)
        vivod_polya()
    if hodd2 == "20" and pole[13] == " ":
        pole.pop(13)
        pole.insert(13, igrok2)
        vivod_polya()
    if hodd2 == "21" and pole[14] == " ":
        pole.pop(14)
        pole.insert(14, igrok2)
        vivod_polya()
    if hodd2 == "22" and pole[15] == " ":
        pole.pop(15)
        pole.insert(15, igrok2)
        vivod_polya()


# 7. Проверка окончания игры
def finish():
    if pole[5] == igrok1 and pole[6] == igrok1 and pole[7] == igrok1 or pole[9] == igrok1 and pole[10] == igrok1 and \
            pole[11] == igrok1 or pole[13] == igrok1 and pole[14] == igrok1 and pole[15] == igrok1 or pole[5] == igrok1 and pole[9] == igrok1 and pole[13] == igrok1 or pole[6] == igrok1 and pole[10] == igrok1 and pole[14] == igrok1 or pole[7] == igrok1 and pole[11] == igrok1 and pole[15] == igrok1 or pole[5] == igrok1 and pole[10] == igrok1 and pole[15] == igrok1 or pole[7] == igrok1 and pole[10] == igrok1 and pole[13] == igrok1:
        print("Игрок 1 - Победитель!")
        quit()
    elif pole[5] == igrok2 and pole[6] == igrok2 and pole[7] == igrok2 or pole[9] == igrok2 and pole[10] == igrok2 and \
            pole[11] == igrok2 or pole[13] == igrok2 and pole[14] == igrok2 and pole[15] == igrok2 or pole[5] == igrok2 and pole[9] == igrok2 and pole[13] == igrok2 or pole[6] == igrok2 and pole[10] == igrok2 and pole[14] == igrok2 or pole[7] == igrok2 and pole[11] == igrok2 and pole[15] == igrok2 or pole[5] == igrok2 and pole[10] == igrok2 and pole[15] == igrok2 or pole[7] == igrok2 and pole[10] == igrok2 and pole[13] == igrok2:
        print("Игрок 2 - Победитель!")
        quit()
    elif pole[5] != " " and pole[6] != " " and pole[7] != " " and pole[9] != " " and pole[10] != " " and pole[11] != " " and pole[13] != " " and pole[14] != " " and pole[15] != " ":
        print("Дружеская ничья!")
        quit()

while finish() != True:
    print("Игрок 1, ваш ход:")
    hod1()
    if finish() != True:
        print("Игрок 2, ваш ход:")
        hod2()
