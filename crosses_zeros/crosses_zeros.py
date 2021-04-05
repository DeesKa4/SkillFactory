border = list(range(1, 10))
win_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                   (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_borders():  # функция для отрисовки границ игры
    print('_____________')
    for i in range(3):
        print('|', border[0 + i * 3], '|', border[1 + i * 3], '|', border[2 + i * 3], '|')
        print('_____________')


def waiting_input(player_sign):  # функция, ожидающая ввода от игрока
    while True:
        print('Введите число от 1 до 9')
        value = input(
            'Куда хотите поставить  |' + player_sign + '| ? - ')  # Ввести число, вкоторое хотим поставить Х или О
        if not (value in '123456789'):  # проверка на правильность ввода
            print()
            print('Невернный ввод. Повторите попытку') # принты, чтобы повысить читаемость вывода в консоли
            print()
            continue
        if str(border[int(value) - 1]) in 'XO':  # проверка на наличие уже поставленного знака
            print()
            print('Эта клетка уже занята')
            print()
            continue
        else:
            border[int(value) - 1] = player_sign  # присвоение клетке игрового поля нужного знака
            break


def check_win():  # функция проверки на выигрышную комбинацию
    while True:
        for each in win_combination:
            if (border[each[0] - 1] == border[each[1] - 1] == border[each[2] - 1]):  # проверка на наличие выигрышной комбинации
                return border[each[1] - 1]
        else:
            return False


def game():  # сама игра
    draw_borders()  # рисуем границы
    steps = 0  # задаем количество ходов
    while True:
        if steps % 2 == 0:  # делим ходы на очередность
            waiting_input('X')
            draw_borders()
        else:
            waiting_input('O')
            draw_borders()
        if steps > 3:
            winner = check_win()
            if winner:  # проверяем на победителя
                print('Выиграл |' + winner + '|. Поздравляю!')
                break
        steps += 1
        if steps > 8:  # если победитель не выявлен, объявляем ничью
            print('Ничья!')


game()
