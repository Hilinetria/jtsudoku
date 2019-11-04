# coding=utf-8
import random
from . import solver

def generate(difficult, example):
    flook = [[0 for j in range(example.n * example.n)] for i in
             range(example.n * example.n)]
    iterator = 0
    while iterator < example.n ** 4:
        i, j = random.randrange(0, example.n * example.n, 1), random.randrange(0,
                                                                               example.n * example.n,
                                                                               1)  # Выбираем случайную ячейку
        if flook[i][j] == 0:  # Если её не смотрели
            iterator += 1
            flook[i][j] = 1  # Посмотрим

            temp = example.table[i][j]  # Сохраним элемент на случай если без него нет решения или их слишком много
            example.table[i][j] = 0
            difficult -= 1  # Усложняем если убрали элемент

            table_solution = []
            for copy_i in range(0, example.n * example.n):
                table_solution.append(
                    example.table[copy_i][:])  # Скопируем в отдельный список

            i_solution = 0
            for solution in solver.solve_sudoku((example.n, example.n),
                                                table_solution):
                i_solution += 1  # Считаем количество решений

            if i_solution != 1:  # Если решение не одинственное вернуть всё обратно
                example.table[i][j] = temp
                difficult += 1  # Облегчаем
