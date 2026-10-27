"""Модуль главного управляющего класса приложения."""

import tkinter as tk
import random
from src.models.animation_model import BallModel
from src.renderers.renderer import CanvasRenderer


class AnimationApp:
    """Класс графического интерфейса и управления циклом анимации."""

    def __init__(self, root: tk.Tk):
        """Настройка главного окна, холста и инициализация объектов.

        :param root: Главное окно tkinter.
        """
        self.root = root
        self.root.title("Лабораторная 2: Упругое столкновение")
        self.root.resizable(False, False)

        # Константы размеров окна
        self.width = 800
        self.height = 600

        # Флаг состояния паузы
        self.is_paused = False

        # Создание холста (черный фон)
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#121212")
        self.canvas.pack()

        # Инициализация рендерера
        self.renderer = CanvasRenderer(self.canvas)

        # Создание объекта модели шара со случайными параметрами
        self.ball = self.create_random_ball()

        # Привязка клавиш клавиатуры для интерактива
        self.root.bind("<Space>", self.toggle_pause)
        self.root.bind("<r>", self.reset_animation)
        self.root.bind("<R>", self.reset_animation)

        # Запуск цикла обновления кадров
        self.update_frame()

    def create_random_ball(self) -> BallModel:
        """Генерация модели шара со случайной скоростью и координатами.

        :return: Экземпляр BallModel.
        """
        radius = 25
        x = random.randint(radius + 10, self.width - radius - 10)
        y = random.randint(radius + 10, self.height - radius - 10)
        speed_x = random.choice([-1, 1]) * random.uniform(4, 8)
        speed_y = random.choice([-1, 1]) * random.uniform(4, 8)

        return BallModel(x, y, radius, speed_x, speed_y)

    def toggle_pause(self, event):
        """Переключение состояния паузы анимации по нажатию Пробела."""
        self.is_paused = not self.is_paused

    def update_frame(self):
        """Основной цикл анимации: расчет физики, очистка экрана и перерисовка."""
        if not self.is_paused:
            self.ball.update_position(self.width, self.height)

        self.canvas.delete("all")
        self.renderer.render_ball(self.ball, color="#FF1493")

        # Планирование следующего кадра (~60 FPS)
        self.root.after(16, self.update_frame)

    def reset_animation(self, event):
        """Сброс параметров объекта в начальное состояние по нажатию клавиши R."""
        self.ball = self.create_random_ball()
