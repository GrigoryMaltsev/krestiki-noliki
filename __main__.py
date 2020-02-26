import argparse
from game import new_game, play, loading
from display import build_field, print_field
from secondary import check_saving, open_helper


def console_reader():
    parser = argparse.ArgumentParser()
    parser.add_argument("--comand", help="Что бы узнать правила игры введите --comand helpme")
    args = parser.parse_args()
    if args.comand == 'helpme':
        open_helper()
    elif args.comand == None:
        pass
    else:
        print('Неизвестная команда\n\n\n')


console_reader()


# ___ЗАПУСК ИГРЫ___

print('Добро пожаловать в игру \"Крести-нолики\"\n')
if check_saving() == 0:
    """
    Нет сохраненной игры
    """
    n, k, player, progress_field = new_game()
    current_field = build_field(n, k)
    print_field(current_field)
    play(player, progress_field, current_field)

else:
    """
    Есть сохраненная игра
    """
    loading()
