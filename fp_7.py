"""
Завдання 7. Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.
Сума	Імовірність
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.
"""

import numpy as np
import matplotlib.pyplot as plt


def roll_dice():
    return np.random.randint(1, 7)


def roll_2_dices():
    return roll_dice() + roll_dice()


def mc_simulation(rolls_num):
    result_rolls = {}
    for i in range(2, 13):
        result_rolls[i] = 0

    for _ in range(rolls_num+1):
        number = roll_2_dices()
        result_rolls[number] += 1

    result_probs = {sum: (rolls / rolls_num)
                    for sum, rolls in result_rolls.items()}

    print(result_rolls)
    print(result_probs)

    return result_probs


def plot_probabilities(result):
    # Створення графіка
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    for idx, (accuracy, data) in enumerate(result.items()):
        sums = list(data.keys())
        probs = list(data.values())
        i = idx // 2
        j = idx % 2

        axes[i, j].bar(sums, probs, tick_label=sums)
        axes[i, j].set_title(
            f"Ймовірність суми чисел на двох кубиках(N={accuracy})")
        axes[i, j].set_xlabel("Сума чисел на кубиках")
        axes[i, j].set_ylabel("Ймовірність")

        # Додавання відсотків випадання на графік
        for n, prob in enumerate(probs):
            axes[i, j].text(sums[n], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()


if __name__ == "__main__":
    result = {}
    for accuracy in [100, 1000, 10000, 100000]:
        result[accuracy] = mc_simulation(accuracy)
    plot_probabilities(result)
