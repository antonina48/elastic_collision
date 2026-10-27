"""Модуль модели физического поведения объектов."""


class BallModel:
    """Класс, описывающий математическую модель движущегося шара."""

    def __init__(self, x: float, y: float, radius: float, speed_x: float, speed_y: float):
        """Инициализация параметров шара.

        :param x: Начальная координата X центра шара.
        :param y: Начальная координата Y центра шара.
        :param radius: Радиус шара.
        :param speed_x: Скорость движения по оси X (пикселей/кадр).
        :param speed_y: Скорость движения по оси Y (пикселей/кадр).
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update_position(self, width: int, height: int):
        """Обновление координат шара с учетом упругого столкновения с границами.

        :param width: Текущая ширина рабочей области (окна анимации).
        :param height: Текущая высота рабочей области (окна анимации).
        """
        # Смещение объекта на величину скорости
        self.x += self.speed_x
        self.y += self.speed_y

        # Проверка столкновения с левой и правой границами экрана
        if self.x - self.radius <= 0:
            self.x = self.radius  # Корректировка позиции во избежание застревания
            self.speed_x = -self.speed_x  # Инверсия скорости (упругий отскок)
        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.speed_x = -self.speed_x

        # Проверка столкновения с верхней и нижней границами экрана
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.speed_y = -self.speed_y
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.speed_y = -self.speed_y
