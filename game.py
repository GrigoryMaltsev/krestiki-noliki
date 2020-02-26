"""
Управление игровым процессом
"""


import pickle
import random
from display import build_field, print_field, rebuild_field
from choices import grin_choice, player_choice, check_win
from secondary import check_valid_input, open_helper


def new_game():
    print(
        'Вы сможете задать произвольный размер поля N K, где N — длина поля, K — ширина поля.\n'
        'Вы играете за "крестики", а против вас за "нолики" будет играть компьютер Grin, очередность ходов будет определяться автоматически.\n'
        'Во время своего хода вам нужно будет указать координату, куда вы хотите поставить крестик в виде двух чисел через запятую, например \"3,3\".\n'
        'Подробнее о правилах можно прочитать в RULES.\n\n'
        'Поехали!'
        )
    n = None
    k = None

    while n == None:
        n = check_valid_input(input())

    while k == None:
        k = check_valid_input(input())

    first_choice = random.randint(0, 1)  # 0 - комп, 1 - игрок
    empty_progress_field = [['free' for x in range(n)] for z in range(k)]

    return n, k, first_choice, empty_progress_field


def play(player, progress_field, current_field):
    if player == 0:
        """
        Ход копьютера
        """
        print('\n Компьютер сходил')
        point, progress_field = grin_choice(progress_field)
        current_field = rebuild_field(current_field, point)
        print_field(current_field)

        if check_win(progress_field, point, player) == 0:
            print('Компьютер Grin выиграл!')
            result = '0'
            return result
        elif check_win(progress_field, point, player) == 'Ничья':
            print('Ничья!')
            result = 'Ничья'
            return result
        else:
            player = 1
            play(player, progress_field, current_field)

    elif player == 1:
        """
        Ход игрока
        """
        print(
            '\n Ваш ход.',
            'Если вы забыли правила - напишите \'helpme\'.',
            'Если хотите сохранить игру - \'save\'.'
        )
        hod = input()
        if hod == 'helpme':
            open_helper()
            play(player, progress_field, current_field)
        elif hod == 'save':
            saving(progress_field, current_field)
            print('Игра сохранена. Продолжить? Y/N')
            temp_descision = input().lower()
            if temp_descision == 'y':
                play(player, progress_field, current_field)
            elif temp_descision == 'n':
                return
            else:
                print('Неизвестная команда')
                play(player, progress_field, current_field)

        elif ',' in hod:  # Валидная команда для хода
            hod = hod.replace(' ', '').split(',')
            if len(hod) == 2:
                line = check_valid_input(hod[0])
                place = check_valid_input(hod[1])
                if ((line != None) and (place != None)) and ((line <= len(progress_field)) and (place <= len(progress_field[0]))):
                    point = [line, place]
                    point, progress_field = player_choice(point, progress_field)
                    if point == None:
                        play(player, progress_field, current_field)
                    current_field = rebuild_field(current_field, point)
                    print_field(current_field)
                    if check_win(progress_field, point, player) == 1:
                        print('Вы победили!')
                        result = '1'
                        return result
                    elif check_win(progress_field, point, player) == 'Ничья':
                        print('Ничья!')
                        result = 'Ничья'
                        return result
                    else:
                        player = 0
                        play(player, progress_field, current_field)
                else:
                    print('Неизвестная команда')
                    play(player, progress_field, current_field)
        else:
            print('Неизвестная команда')
            play(player, progress_field, current_field)


def saving(progress_field, current_field):
    with open('dumps/data.pickle', 'wb') as f:
        pickle.dump([progress_field, current_field], f)


def loading():
        print(
            "У вас есть сохраненная игра. Хотите её загрузить?\n"
            "Если да, нажмите Y.\n"
            "Если хотите начать новую, нажмите N"
            )
        want_loading = input()
        if want_loading.lower() == 'y':
            with open('dumps/data.pickle', 'rb') as f:
                data_load = pickle.load(f)
                progress_field = data_load[0]
                current_field = data_load[1]
                print_field(current_field)
                player = 1
                play(player, progress_field, current_field)
        elif want_loading.lower() == 'n':
            n, k, player, progress_field = new_game()
            current_field = build_field(n, k)
            print_field(current_field)
            play(player, progress_field, current_field)
        else:
            print('Ошибка ввода. Нужно ввести букву \'Y\' или букву \'N\' без кавычев и других символов')
            loading()
