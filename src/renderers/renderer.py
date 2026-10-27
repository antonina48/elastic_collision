"""Модуль графического рендеринга объектов."""

import tkinter as tk
from src.models.animation_model import BallModel


class CanvasRenderer:
    """Класс, отвечающий за визуализацию объектов на графическом холсте."""

    def __init__(self, canvas: tk.Canvas):
        """Инициализация рендерера.

        :param canvas: Компонент холста tkinter для рисования.
        """
        self.canvas = canvas

    def render_ball(self, ball: BallModel, color: str = "#FF1493") -> int:
        """Отрисовка круглого объекта (шара) по его математическим координатам.

        :param ball: Экземпляр модели BallModel.
        :param color: Цвет заливки шара в формате HEX.
        :return: Идентификатор созданного графического объекта на холсте.
        """
        # Вычисление координат описывающего прямоугольника
        x1 = ball.x - ball.radius
        y1 = ball.y - ball.radius
        x2 = ball.x + ball.radius
        y2 = ball.y + ball.radius

        # Создание круга на холсте с белой обводкой
        return self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="white", width=2)
