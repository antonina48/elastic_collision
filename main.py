"""Главная точка входа в приложение."""

import tkinter as tk
from src.app import AnimationApp


def main():
    """Инициализация графической библиотеки и запуск приложения."""
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
