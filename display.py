"""
Отображение игрового поля
"""


def build_field(n, k):
        """
        Создаем новое поле N x K, например 4 х 3

            1  2  3  4
          +--+--+--+--+
        1 |  |  |  |  |
          +--+--+--+--+
        2 |  |  |  |  |
          +--+--+--+--+
        3 |  |  |  |  |
          +--+--+--+--+
        """
        empty_field = {0: ['   '] + [str(x) + " " for x in range(1, n+1)]}
        i = 1
        while i < 2*k:
            empty_field.update(
                {
                    i: [' '] + ["+--"*n + "+"],
                    i+1: [int((i+1)/2)] + ["| "]*n + ['|']
                }
            )
            i += 2
        empty_field.update(
            {i: [' '] + ["+--"*n + "+"]}
        )

        return empty_field


def print_field(current_field):
    for i in range(len(current_field)):
        print(*current_field.get(i))


def rebuild_field(current_field, point):
    current_field.get(point[0]*2).pop(point[1])
    current_field.get(point[0]*2).insert(point[1], '|'+point[2])
    return current_field
