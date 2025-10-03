"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import matplotlib.pyplot as plt
import numpy as np
import math


class PythagorasTree:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 1, figsize=(12, 10))

    def draw_line(self, bottom_x, bottom_y, top_x, top_y, level):
        plt.plot([bottom_x, top_x], [bottom_y, top_y],
                 'r-', linewidth=2)

    def pythagoras_tree(self, x1, y1, x2, y2, level, max_level):
        if level > max_level:
            return

        self.draw_line(x1, y1, x2, y2, level)

        if level < max_level:

            dx = x2 - x1
            dy = y2 - y1
            len_base = math.sqrt(dx**2 + dy**2)
            len_side = math.sqrt((len_base**2)/2)
            height = math.sqrt((len_side**2)/2)

            angle_rad = math.radians(45)
            scale = 0.7

            new_length = len_base * scale

            current_angle = math.atan2(dy, dx)

            # Ліва гілка (поворот на +45°)
            left_angle = current_angle + angle_rad
            left_x = x2 + new_length * math.cos(left_angle)
            left_y = y2 + new_length * math.sin(left_angle)

            # Права гілка (поворот на -45°)
            right_angle = current_angle - angle_rad
            right_x = x2 + new_length * math.cos(right_angle)
            right_y = y2 + new_length * math.sin(right_angle)

            # Рекурсивно створюємо дві менші гілки
            self.pythagoras_tree(x2, y2, left_x, left_y, level + 1, max_level)
            self.pythagoras_tree(x2, y2, right_x, right_y,
                                 level + 1, max_level)

    def create_tree(self, level=5):
        self.ax.clear()

        bottom_x, bottom_y = 0, 0
        top_x, top_y = 0, 2

        self.pythagoras_tree(bottom_x, bottom_y, top_x, top_y, 0, level)

        self.ax.set_aspect('equal')
        self.ax.set_title(
            f'Дерево Піфагора (Рівень рекурсии: {level})', fontsize=14, fontweight='bold')

        self.ax.autoscale()

        plt.tight_layout()

    def show(self):
        plt.show()


def main():
    tree = PythagorasTree()

    try:
        level = int(input("Enter level of recursion: "))
        if level < 0:
            print("Level must be > 0")
            level = 5
    except ValueError:
        print("Error: Wrong input")
        level = 5

    tree.create_tree(level)
    tree.show()


if __name__ == "__main__":
    main()
