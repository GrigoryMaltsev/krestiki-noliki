"""
Механика ходов
"""


def grin_choice(progress_field):
    for line in range(len(progress_field)):
        for place in range(len(progress_field[line])):
            if progress_field[line][place] == 'free':
                progress_field[line].pop(place)
                progress_field[line].insert(place, 0)
                point = [line+1, place+1, '0']
                return point, progress_field


def player_choice(point, progress_field):
    line = int(point[0]) - 1
    place = int(point[1]) - 1
    if progress_field[line][place] == 'free':
        progress_field[line].pop(place)
        progress_field[line].insert(place, 1)
        point = [line+1, place+1, 'X']
    else:
        print('Выбранное поле несвободно')
        point = None
    return point, progress_field


def check_win(progress_field, point, player):
    condition = min(len(progress_field), len(progress_field[0]))
    result = None
    result = check_win_horizont(player, point, condition, progress_field)
    if result == None:
        result = check_win_vert(player, point, condition, progress_field)
        if result == None:
            result = check_win_x(player, point, condition, progress_field)
            if check_win_nobody(progress_field) == True:
                return 'Ничья'
            return result
        else:
            return result
    else:
        return result


def check_win_horizont(player, point, condition, progress_field):
    """
    По горизонтали. Проверка такая сложная, потому что поле может быть прямоугольным
    """
    count = 0
    line = point[0] - 1
    place = point[1] - 1
    result = None
    while place < len(progress_field[line]):  # Идем вправо
        if progress_field[line][place] == player:
            count += 1
            place += 1
            if count == condition:
                result = player
                return result
        else:
            break
    place = point[1] - 2
    while place >= 0:  # Идем влево
        if progress_field[line][place] == player:
            count += 1
            place -= 1
            if count == condition:
                result = player
                return result
        else:
            break
    return result


def check_win_vert(player, point, condition, progress_field):
    """
    По вертикали. Проверка такая сложная, потому что поле может быть прямоугольным
    """
    count = 0
    line = point[0] - 1
    place = point[1] - 1
    result = None
    while line < len(progress_field):  # Идем вниз
        if progress_field[line][place] == player:
            count += 1
            line += 1
            if count == condition:
                result = player
                break
        else:
            break
    line = point[0] - 2
    while line >= 0:  # Идем вверх
        if progress_field[line][place] == player:
            count += 1
            line -= 1
            if count == condition:
                result = player
                break
        else:
            break

    return result


def check_win_x(player, point, condition, progress_field):
    """
    По диагонали. Проверка такая сложная, потому что поле может быть прямоугольным
    """
    count = 0
    line = point[0] - 1
    place = point[1] - 1
    result = None
    while (line < len(progress_field)) and (place < len(progress_field[line])):  # Идем вниз вправо
        if progress_field[line][place] == player:
            count += 1
            line += 1
            place += 1
            if count == condition:
                result = player
                return result
        else:
            break
    line = point[0] - 2
    place = point[1] - 2
    while (line >= 0) and (place >= 0):  # Идем вверх влево
        if progress_field[line][place] == player:
            count += 1
            line -= 1
            place -= 1
            if count == condition:
                result = player
                return result
        else:
            break
    if result == player:
        return result

    else:
        """
        Смотрим вторую диагональ. Проверка такая сложная, потому что поле может быть прямоугольным
        """
        count = 0
        line = point[0] - 1
        place = point[1] - 1
        result = None
        while (line < len(progress_field)) and (place >= 0):  # Идем вниз влево
            if progress_field[line][place] == player:
                count += 1
                line += 1
                place -= 1
                if count == condition:
                    result = player
                    return result
            else:
                break
        line = point[0] - 2
        place = point[1]
        while (line >= 0) and (place < len(progress_field[line])):  # Идем вверх вправо
            if progress_field[line][place] == player:
                count += 1
                line -= 1
                place += 1
                if count == condition:
                    result = player
                    return result
            else:
                break
    return result


def check_win_nobody(progress_field):
    for item in progress_field:
        if 'free' not in item:
            nobody = True
        else:
            nobody = False
    return nobody
